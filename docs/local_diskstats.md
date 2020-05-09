
# local_diskstats
```python
local_diskstats(volname=None)
```

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

