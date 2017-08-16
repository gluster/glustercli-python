from gluster.cli import volume

UUID_FILE = "/var/lib/glusterd/glusterd.info"

myuuid = None


def get_node_id():
    global myuuid

    if myuuid is not None:
        return myuuid

    val = None
    with open(UUID_FILE) as f:
        for line in f:
            if line.startswith("UUID="):
                val = line.strip().split("=")[-1]
                break

    myuuid = val
    return val


def get_local_bricks(volname=None):
    local_node_id = get_node_id()
    volinfo = volume.info(volname)
    bricks = []
    for idx, vol in enumerate(volinfo):
        for jdx, brick in enumerate(vol["bricks"]):
            if brick["uuid"] != local_node_id:
                continue

            bricks.append({
                "volume": vol["name"],
                "brick_index": jdx,
                "node_id": brick["uuid"],
                "brick": brick["name"]})

    return bricks
