import os

from utils import get_local_bricks


def local_utilization(volname=None):
    local_bricks = get_local_bricks(volname)

    for brick in local_bricks:
        bpath = brick["brick"].split(":", 1)[-1]
        st = os.statvfs(bpath)

        brick["block_size"] = st.f_frsize
        brick["blocks_total"] = st.f_blocks
        brick["blocks_free"] = st.f_bfree
        brick["blocks_avail"] = st.f_bavail
        brick["inodes_total"] = st.f_files
        brick["inodes_free"] = st.f_ffree
        brick["inodes_avail"] = st.f_favail

    return local_bricks
