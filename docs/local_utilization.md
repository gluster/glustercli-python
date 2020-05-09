
# local_utilization
```python
local_utilization(volname=None)
```

Collect Utilization details of local bricks

:param volname: Volume Name
:returns: List of utilization information
    {
        "volume": VOLUME_NAME,
        "brick_index": BRICK_INDEX_IN_VOL_INFO,
        "node_id": NODE_ID,
        "brick": BRICK_NAME,
        "block_size": ST_F_FRSIZE,
        "blocks_total": ST_F_BLOCKS,
        "blocks_free": ST_F_BFREE,
        "blocks_avail": ST_F_BAVAIL,
        "inodes_total": ST_F_FILES,
        "inodes_free": ST_F_FFREE,
        "inodes_avail": ST_F_FAVAIL
    }

