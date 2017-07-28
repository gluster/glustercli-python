import os
import subprocess

from utils import get_local_bricks


default_diskstat = {
    "major_number": 0,
    "minor_number": 0,
    "reads_completed": 0,
    "reads_merged": 0,
    "sectors_read": 0,
    "time_spent_reading": 0,
    "writes_completed": 0,
    "writes_merged": 0,
    "sectors_written": 0,
    "time_spent_writing": 0,
    "ios_currently_in_progress": 0,
    "time_spent_doing_ios": 0,
    "weighted_time_spent_doing_ios": 0
}


def local_diskstats(volname=None):
    """
    Collect Diskstats info of local bricks

    :param volname: Volume Name
    :returns: List of diskstats information
        {
            "volume": VOLUME_NAME,
            "brick_index": BRICK_INDEX_IN_VOL_INFO,
            "node_id": NODE_ID,
            "brick": BRICK_NAME,
            "fs": BRICK_FILESYSTEM,
            "device": BRICK_DEVICE,
            "major_number": MAJOR_NUMBER,
            "minor_number": MINOR_NUMBER,
            "reads_completed": READS_COMPLETED,
            "reads_merged": READS_MERGED,
            "sectors_read": SECTORS_READ,
            "time_spent_reading": TIME_SPENT_READING,
            "writes_completed": WRITES_COMPLETED,
            "writes_merged": WRITES_MERGED,
            "sectors_written": SECTORS_WRITTEN,
            "time_spent_writing": TIME_SPENT_WRITING,
            "ios_currently_in_progress": IOS_CURRENTLY_IN_PROGRESS,
            "time_spent_doing_ios": TIME_SPENT_DOING_IOS,
            "weighted_time_spent_doing_ios": WEIGHTED_TIME_SPENT_DOING_IOS
        }
    """
    local_bricks = get_local_bricks(volname)
    cmd = ["df", "--output=source"]

    diskstat_data_raw = ""
    with open("/proc/diskstats") as f:
        diskstat_data_raw = f.read()

    # /proc/diskstats fields
    #  1 - major number
    #  2 - minor mumber
    #  3 - device name
    #  4 - reads completed successfully
    #  5 - reads merged
    #  6 - sectors read
    #  7 - time spent reading (ms)
    #  8 - writes completed
    #  9 - writes merged
    # 10 - sectors written
    # 11 - time spent writing (ms)
    # 12 - I/Os currently in progress
    # 13 - time spent doing I/Os (ms)
    # 14 - weighted time spent doing I/Os (ms)
    diskstat_data = {}
    for d in diskstat_data_raw.strip().split("\n"):
        d = d.split()
        if not d:
            continue

        diskstat_data[d[2]] = {
            "major_number": d[0],
            "minor_number": d[1],
            "reads_completed": d[3],
            "reads_merged": d[4],
            "sectors_read": d[5],
            "time_spent_reading": d[6],
            "writes_completed": d[7],
            "writes_merged": d[8],
            "sectors_written": d[9],
            "time_spent_writing": d[10],
            "ios_currently_in_progress": d[11],
            "time_spent_doing_ios": d[12],
            "weighted_time_spent_doing_ios": d[13]
        }

    for brick in local_bricks:
        bpath = brick["brick"].split(":", 1)[-1]
        p = subprocess.Popen(cmd + [bpath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, _ = p.communicate()

        # `df` command error
        if p.returncode != 0:
            brick["fs"] = "unknown"
            brick["device"] = "unknown"
            brick.update(default_diskstat)
            continue

        df_data = out.strip()
        df_data = df_data.split("\n")[-1].strip()  # First line is header
        brick["fs"] = df_data
        if os.path.islink(df_data):
            brick["device"] = os.readlink(df_data).split("/")[-1]
        else:
            brick["device"] = df_data.split("/")[-1]

        brick.update(diskstat_data.get(brick["device"], default_diskstat))


    return local_bricks
