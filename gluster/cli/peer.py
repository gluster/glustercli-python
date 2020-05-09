# -*- coding: utf-8 -*-

from .utils import peer_execute, peer_execute_xml, gluster_execute_xml, GlusterCmdException
from .parsers import parse_peer_status, parse_pool_list


def probe(host):
    """
    Add Host to Cluster

    :param host: Hostname or IP
    :returns: Output of peer probe command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["probe", host]
    return peer_execute(cmd)


def attach(host):
    """
    Add Host to Cluster, alias for probe

    :param host: Hostname or IP
    :returns: Output of peer probe command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    return probe(host)


def detach(host):
    """
    Remove Host from Cluster

    :param host: Hostname or IP
    :returns: Output of peer detach command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["detach", host]
    return peer_execute(cmd)


def detach_all():
    """
    Removes All Hosts from Cluster

    :returns: Output of peer detach command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    peers = parse_peer_status(peer_execute_xml(["status"]))
    errors_list = []
    outlist = []
    if len(peers) > 0:
        for peer in peers:
            host = peer["hostname"]
            if peer["connected"] == "Connected":
                cmd = ["detach", host]
                try:
                    result = peer_execute(cmd)
                    out = str(host) + " " + result.decode()
                    outlist.append(out)
                except Exception as err:
                    errors_list.append(err)
            else:
                err = str(host) + " is not connected"
                errors_list.append(err)
    if len(errors_list):
        raise GlusterCmdException((1, "", errors_list))
    return "\n".join(outlist)


def status():
    """
    Peer Status of Cluster

    :returns: Output of peer status command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["status"]
    return parse_peer_status(peer_execute_xml(cmd))


def pool():
    """
    Cluster Pool Status

    :returns: Pool list and status, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["pool", "list"]
    return parse_pool_list(gluster_execute_xml(cmd))
