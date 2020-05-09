# -*- coding: utf-8 -*-

import xml.etree.cElementTree as etree

ParseError = etree.ParseError if hasattr(etree, 'ParseError') else SyntaxError


class GlusterCmdOutputParseError(Exception):
    pass


def _parse_a_vol(volume_el):
    value = {
        'name': volume_el.find('name').text,
        'uuid': volume_el.find('id').text,
        'type': volume_el.find('typeStr').text.upper().replace('-', '_'),
        'status': volume_el.find('statusStr').text,
        'num_bricks': int(volume_el.find('brickCount').text),
        'distribute': int(volume_el.find('distCount').text),
        'stripe': int(volume_el.find('stripeCount').text),
        'replica': int(volume_el.find('replicaCount').text),
        'transport': volume_el.find('transport').text,
        'bricks': [],
        'options': []
    }

    if value['transport'] == '0':
        value['transport'] = 'TCP'
    elif value['transport'] == '1':
        value['transport'] = 'RDMA'
    else:
        value['transport'] = 'TCP,RDMA'

    for brick in volume_el.findall('bricks/brick'):
        value['bricks'].append({"name": brick.find("name").text,
                                "uuid": brick.find("hostUuid").text})

    for opt in volume_el.findall('options/option'):
        value['options'].append({"name": opt.find('name').text,
                                 "value": opt.find('value').text})

    return value


def parse_volume_info(info):
    tree = etree.fromstring(info)
    volumes = []
    for volume_el in tree.findall('volInfo/volumes/volume'):
        try:
            volumes.append(_parse_a_vol(volume_el))
        except (ParseError, AttributeError, ValueError) as err:
            raise GlusterCmdOutputParseError(err)

    return volumes


def _parse_a_node(node_el):
    brick_path = (node_el.find('hostname').text + ":" + node_el.find('path').text)
    value = {
        'name': brick_path,
        'uuid': node_el.find('peerid').text,
        'online': True if node_el.find('status').text == "1" else False,
        'pid': node_el.find('pid').text,
        'size_total': node_el.find('sizeTotal').text,
        'size_free': node_el.find('sizeFree').text,
        'device': node_el.find('device').text,
        'block_size': node_el.find('blockSize').text,
        'mnt_options': node_el.find('mntOptions').text,
        'fs_name': node_el.find('fsName').text,
    }

    # ISSUE #14 glusterfs 3.6.5 does not have 'ports' key
    # in vol status detail xml output
    if node_el.find('ports'):
        value['ports'] = {
            "tcp": node_el.find('ports').find("tcp").text,
            "rdma": node_el.find('ports').find("rdma").text
        }
    else:
        value['ports'] = {
            "tcp": node_el.find('port'),
            "rdma": None
        }

    return value


def _parse_volume_status(data):
    tree = etree.fromstring(data)
    nodes = []
    for node_el in tree.findall('volStatus/volumes/volume/node'):
        try:
            nodes.append(_parse_a_node(node_el))
        except (ParseError, AttributeError, ValueError) as err:
            raise GlusterCmdOutputParseError(err)

    return nodes


def parse_volume_status(status_data, volinfo):
    nodes_data = _parse_volume_status(status_data)
    tmp_brick_status = {}
    for node in nodes_data:
        tmp_brick_status[node["name"]] = node

    volumes = []
    for vol in volinfo:
        volumes.append(vol.copy())
        volumes[-1]["bricks"] = []

        for brick in vol["bricks"]:
            brick_status_data = tmp_brick_status.get(brick["name"], None)
            if brick_status_data is None:
                # Default Status
                volumes[-1]["bricks"].append({
                    "name": brick["name"],
                    "uuid": brick["uuid"],
                    "online": False,
                    "ports": {"tcp": "N/A", "rdma": "N/A"},
                    "pid": "N/A",
                    "size_total": "N/A",
                    "size_free": "N/A",
                    "device": "N/A",
                    "block_size": "N/A",
                    "mnt_options": "N/A",
                    "fs_name": "N/A"
                })
            else:
                volumes[-1]["bricks"].append(brick_status_data.copy())

    return volumes


def _parse_profile_info_clear(volume_el):
    clear = {
        'volname': volume_el.find('volname').text,
        'bricks': []
    }

    for brick_el in volume_el.findall('brick'):
        clear['bricks'].append({'brick_name': brick_el.find('brickName').text,
                                'clear_stats': brick_el.find('clearStats').text})

    return clear


def _bytes_size(size):
    traditional = [
        (1024**5, 'PB'),
        (1024**4, 'TB'),
        (1024**3, 'GB'),
        (1024**2, 'MB'),
        (1024**1, 'KB'),
        (1024**0, 'B')
    ]

    for factor, suffix in traditional:
        if size > factor:
            break
    return str(int(size / factor)) + suffix


def _parse_profile_block_stats(b_el):
    stats = []
    for block_el in b_el.findall('block'):
        size = _bytes_size(int(block_el.find('size').text))
        stats.append({size: {'reads': int(block_el.find('reads').text),
                             'writes': int(block_el.find('writes').text)}})
    return stats


def _parse_profile_fop_stats(fop_el):
    stats = []
    for fop in fop_el.findall('fop'):
        name = fop.find('name').text
        stats.append(
            {
                name: {
                    'hits': int(fop.find('hits').text),
                    'max_latency': float(fop.find('maxLatency').text),
                    'min_latency': float(fop.find('minLatency').text),
                    'avg_latency': float(fop.find('avgLatency').text),
                }
            }
        )
    return stats


def _parse_profile_bricks(brick_el):
    cumulative_block_stats = []
    cumulative_fop_stats = []
    cumulative_total_read_bytes = 0
    cumulative_total_write_bytes = 0
    cumulative_total_duration = 0

    interval_block_stats = []
    interval_fop_stats = []
    interval_total_read_bytes = 0
    interval_total_write_bytes = 0
    interval_total_duration = 0

    brick_name = brick_el.find('brickName').text

    if brick_el.find('cumulativeStats') is not None:
        cumulative_block_stats = _parse_profile_block_stats(
            brick_el.find('cumulativeStats/blockStats'))
        cumulative_fop_stats = _parse_profile_fop_stats(
            brick_el.find('cumulativeStats/fopStats'))
        cumulative_total_read_bytes = int(
            brick_el.find('cumulativeStats').find('totalRead').text)
        cumulative_total_write_bytes = int(
            brick_el.find('cumulativeStats').find('totalWrite').text)
        cumulative_total_duration = int(
            brick_el.find('cumulativeStats').find('duration').text)

    if brick_el.find('intervalStats') is not None:
        interval_block_stats = _parse_profile_block_stats(
            brick_el.find('intervalStats/blockStats'))
        interval_fop_stats = _parse_profile_fop_stats(
            brick_el.find('intervalStats/fopStats'))
        interval_total_read_bytes = int(
            brick_el.find('intervalStats').find('totalRead').text)
        interval_total_write_bytes = int(
            brick_el.find('intervalStats').find('totalWrite').text)
        interval_total_duration = int(
            brick_el.find('intervalStats').find('duration').text)

    profile_brick = {
        'brick_name': brick_name,
        'cumulative_block_stats': cumulative_block_stats,
        'cumulative_fop_stats': cumulative_fop_stats,
        'cumulative_total_read_bytes': cumulative_total_read_bytes,
        'cumulative_total_write_bytes': cumulative_total_write_bytes,
        'cumulative_total_duration': cumulative_total_duration,
        'interval_block_stats': interval_block_stats,
        'interval_fop_stats': interval_fop_stats,
        'interval_total_read_bytes': interval_total_read_bytes,
        'interval_total_write_bytes': interval_total_write_bytes,
        'interval_total_duration': interval_total_duration,
    }

    return profile_brick


def _parse_profile_info(volume_el):
    profile = {
        'volname': volume_el.find('volname').text,
        'bricks': []
    }

    for brick_el in volume_el.findall('brick'):
        profile['bricks'].append(_parse_profile_bricks(brick_el))

    return profile


def parse_volume_profile_info(info, opt):
    xml = etree.fromstring(info)
    profiles = []
    for prof_el in xml.findall('volProfile'):
        try:
            if opt == "clear":
                profiles.append(_parse_profile_info_clear(prof_el))
            else:
                profiles.append(_parse_profile_info(prof_el))

        except (ParseError, AttributeError, ValueError) as err:
            raise GlusterCmdOutputParseError(err)

    return profiles


def parse_volume_options(data):
    raise NotImplementedError("Volume Options")


def parse_georep_status(data, volinfo):
    """
    Merge Geo-rep status and Volume Info to get Offline Status
    and to sort the status in the same order as of Volume Info
    """
    session_keys = set()
    gstatus = {}

    try:
        tree = etree.fromstring(data)
        # Get All Sessions
        for volume_el in tree.findall("geoRep/volume"):
            sessions_el = volume_el.find("sessions")
            # Master Volume name if multiple Volumes
            mvol = volume_el.find("name").text

            # For each session, collect the details
            for session in sessions_el.findall("session"):
                session_slave = "{0}:{1}".format(mvol, session.find(
                    "session_slave").text)
                session_keys.add(session_slave)
                gstatus[session_slave] = {}

                for pair in session.findall('pair'):
                    master_brick = "{0}:{1}".format(
                        pair.find("master_node").text,
                        pair.find("master_brick").text
                    )

                    gstatus[session_slave][master_brick] = {
                        "mastervol": mvol,
                        "slavevol": pair.find("slave").text.split("::")[-1],
                        "master_node": pair.find("master_node").text,
                        "master_brick": pair.find("master_brick").text,
                        "slave_user": pair.find("slave_user").text,
                        "slave": pair.find("slave").text,
                        "slave_node": pair.find("slave_node").text,
                        "status": pair.find("status").text,
                        "crawl_status": pair.find("crawl_status").text,
                        "entry": pair.find("entry").text,
                        "data": pair.find("data").text,
                        "meta": pair.find("meta").text,
                        "failures": pair.find("failures").text,
                        "checkpoint_completed": pair.find(
                            "checkpoint_completed").text,
                        "master_node_uuid": pair.find("master_node_uuid").text,
                        "last_synced": pair.find("last_synced").text,
                        "checkpoint_time": pair.find("checkpoint_time").text,
                        "checkpoint_completion_time":
                        pair.find("checkpoint_completion_time").text
                    }
    except (ParseError, AttributeError, ValueError) as err:
        raise GlusterCmdOutputParseError(err)

    # Get List of Bricks for each Volume
    all_bricks = {}
    for vol in volinfo:
        all_bricks[vol["name"]] = vol["bricks"]

    # For Each session Get Bricks info for the Volume and Populate
    # Geo-rep status for that Brick
    out = []
    for session in session_keys:
        mvol, _, slave = session.split(":", 2)
        slave = slave.replace("ssh://", "")
        master_bricks = all_bricks[mvol]
        out.append([])
        for brick in master_bricks:
            bname = brick["name"]
            if gstatus.get(session) and gstatus[session].get(bname, None):
                out[-1].append(gstatus[session][bname])
            else:
                # Offline Status
                node, brick_path = bname.split(":")
                if "@" not in slave:
                    slave_user = "root"
                else:
                    slave_user, _ = slave.split("@")

                out[-1].append({
                    "mastervol": mvol,
                    "slavevol": slave.split("::")[-1],
                    "master_node": node,
                    "master_brick": brick_path,
                    "slave_user": slave_user,
                    "slave": slave,
                    "slave_node": "N/A",
                    "status": "Offline",
                    "crawl_status": "N/A",
                    "entry": "N/A",
                    "data": "N/A",
                    "meta": "N/A",
                    "failures": "N/A",
                    "checkpoint_completed": "N/A",
                    "master_node_uuid": brick["uuid"],
                    "last_synced": "N/A",
                    "checkpoint_time": "N/A",
                    "checkpoint_completion_time": "N/A"
                })
    return out


def parse_bitrot_scrub_status(data):
    raise NotImplementedError("Bitrot Scrub Status")


def parse_rebalance_status(data):
    raise NotImplementedError("Rebalance Status")


def parse_quota_list_paths(data):
    raise NotImplementedError("Quota List Paths")


def parse_quota_list_objects(data):
    raise NotImplementedError("Quota List Objects")


def parse_georep_config(data):
    raise NotImplementedError("Georep Config")


def parse_remove_brick_status(status):
    tree = etree.fromstring(status)

    result = {'nodes': [], 'aggregate': _parse_remove_aggregate(
        tree.find('volRemoveBrick/aggregate'))}

    for node_el in tree.findall('volRemoveBrick/node'):
        result['nodes'].append(_parse_remove_node(node_el))

    return result


def _parse_remove_node(node_el):
    value = {
        'name': node_el.find('nodeName').text,
        'id': node_el.find('id').text,
        'files': node_el.find('files').text,
        'size': node_el.find('size').text,
        'lookups': node_el.find('lookups').text,
        'failures': node_el.find('failures').text,
        'skipped': node_el.find('skipped').text,
        'status_code': node_el.find('status').text,
        'status': node_el.find('statusStr').text,
        'runtime': node_el.find('runtime').text
    }

    return value


def _parse_remove_aggregate(aggregate_el):
    value = {
        'files': aggregate_el.find('files').text,
        'size': aggregate_el.find('size').text,
        'lookups': aggregate_el.find('lookups').text,
        'failures': aggregate_el.find('failures').text,
        'skipped': aggregate_el.find('skipped').text,
        'status_code': aggregate_el.find('status').text,
        'status': aggregate_el.find('statusStr').text,
        'runtime': aggregate_el.find('runtime').text
    }

    return value


def parse_tier_detach(data):
    raise NotImplementedError("Tier detach Status")


def parse_tier_status(data):
    raise NotImplementedError("Tier Status")


def parse_volume_list(data):
    xml = etree.fromstring(data)
    volumes = []
    for volume_el in xml.findall('volList/volume'):
        volumes.append(volume_el.text)
    return volumes


def parse_heal_info(data):
    xml = etree.fromstring(data)
    healinfo = []
    for brick_el in xml.findall('healInfo/bricks/brick'):
        healinfo.append({
            'name': brick_el.find('name').text,
            'status': brick_el.find('status').text,
            'host_uuid': brick_el.attrib['hostUuid'],
            'nr_entries': brick_el.find('numberOfEntries').text
        })
    return healinfo


def parse_heal_statistics(data):
    raise NotImplementedError("Heal Statistics")


def parse_snapshot_status(data):
    raise NotImplementedError("Snapshot Status")


def parse_snapshot_info(data):
    raise NotImplementedError("Snapshot Info")


def parse_snapshot_list(data):
    xml = etree.fromstring(data)
    snapshots = []
    for snap_el in xml.findall('snapList/snapshot'):
        snapshots.append(snap_el.text)
    return snapshots


def _parse_a_peer(peer):
    value = {
        'uuid': peer.find('uuid').text,
        'hostname': peer.find('hostname').text,
        'connected': peer.find('connected').text
    }

    if value['connected'] == '0':
        value['connected'] = "Disconnected"
    elif value['connected'] == '1':
        value['connected'] = "Connected"

    return value


def parse_peer_status(data):
    tree = etree.fromstring(data)
    peers = []
    for peer_el in tree.findall('peerStatus/peer'):
        try:
            peers.append(_parse_a_peer(peer_el))
        except (ParseError, AttributeError, ValueError) as err:
            raise GlusterCmdOutputParseError(err)

    return peers


def parse_pool_list(data):
    tree = etree.fromstring(data)
    pools = []
    for peer_el in tree.findall('peerStatus/peer'):
        try:
            pools.append(_parse_a_peer(peer_el))
        except (ParseError, AttributeError, ValueError) as err:
            raise GlusterCmdOutputParseError(err)

    return pools
