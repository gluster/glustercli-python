
# glustercli.cli.volume


## start
```python
start(volname, force=False)
```

Start Gluster Volume

:param volname: Volume Name
:param force: (True|False) Start Volume with Force option
:returns: Output of Start command, raises
 GlusterCmdException((rc, out, err)) on error


## stop
```python
stop(volname, force=False)
```

Stop Gluster Volume

:param volname: Volume Name
:param force: (True|False) Stop Volume with Force option
:returns: Output of Stop command, raises
 GlusterCmdException((rc, out, err)) on error


## restart
```python
restart(volname, force=False)
```

Restart Gluster Volume, Wrapper around two calls stop and start

:param volname: Volume Name
:param force: (True|False) Restart Volume with Force option
:returns: Output of Start command, raises
 GlusterCmdException((rc, out, err)) on error


## delete
```python
delete(volname)
```

Delete Gluster Volume

:param volname: Volume Name
:returns: Output of Delete command, raises
 GlusterCmdException((rc, out, err)) on error


## create
```python
create(volname,
       volbricks,
       replica=0,
       stripe=0,
       arbiter=0,
       disperse=0,
       disperse_data=0,
       redundancy=0,
       transport='tcp',
       force=False)
```

Create Gluster Volume

:param volname: Volume Name
:param volbricks: List of Brick paths(HOSTNAME:PATH)
:param replica: Number of Replica bricks
:param stripe: Number of Stripe bricks
:param arbiter: Number of Arbiter bricks
:param disperse: Number of disperse bricks
:param disperse_data: Number of disperse data bricks
:param redundancy: Number of Redundancy bricks
:param transport: Transport mode(tcp|rdma|tcp,rdma)
:param force: (True|False) Create Volume with Force option
:returns: Output of Create command, raises
 GlusterCmdException((rc, out, err)) on error


## info
```python
info(volname=None, group_subvols=False)
```

Get Gluster Volume Info

:param volname: Volume Name
:param group_subvols: Show Subvolume Information in Groups
:returns: Returns Volume Info, raises
 GlusterCmdException((rc, out, err)) on error


## status_detail
```python
status_detail(volname=None, group_subvols=False)
```

Get Gluster Volume Status

:param volname: Volume Name
:param group_subvols: Show Subvolume Information in Groups
:returns: Returns Volume Status, raises
 GlusterCmdException((rc, out, err)) on error


## optset
```python
optset(volname, opts)
```

Set Volume Options

:param volname: Volume Name
:param opts: Dict with config key as dict key and config value as value
:returns: Output of Volume Set command, raises
 GlusterCmdException((rc, out, err)) on error


## optget
```python
optget(volname, opt='all')
```

Get Volume Options

:param volname: Volume Name
:param opt: Option Name
:returns: List of Volume Options, raises
 GlusterCmdException((rc, out, err)) on error


## optreset
```python
optreset(volname, opt=None, force=False)
```

Reset Volume Options

:param volname: Volume Name
:param opt: Option name to reset, else reset all
:param force: Force reset options
:returns: Output of Volume Reset command, raises
 GlusterCmdException((rc, out, err)) on error


## vollist
```python
vollist()
```

Volumes List

:returns: List of Volumes, raises
 GlusterCmdException((rc, out, err)) on error


## log_rotate
```python
log_rotate(volname, brick)
```

Brick log rotate

:param volname: Volume Name
:param brick: Brick Path
:returns: Output of Log rotate command, raises
 GlusterCmdException((rc, out, err)) on error


## sync
```python
sync(hostname, volname=None)
```

Sync the volume information from a peer

:param hostname: Hostname to sync from
:param volname: Volume Name
:returns: Output of Sync command, raises
 GlusterCmdException((rc, out, err)) on error


## clear_locks
```python
clear_locks(volname,
            path,
            kind,
            inode_range=None,
            entry_basename=None,
            posix_range=None)
```

Clear locks held on path

:param volname: Volume Name
:param path: Locked Path
:param kind: Lock Kind(blocked|granted|all)
:param inode_range: Inode Range
:param entry_basename: Entry Basename
:param posix_range: Posix Range
:returns: Output of Clear locks command, raises
 GlusterCmdException((rc, out, err)) on error


## barrier_enable
```python
barrier_enable(volname)
```

Enable Barrier

:param volname: Volume Name
:returns: Output of Barrier command, raises
 GlusterCmdException((rc, out, err)) on error


## barrier_disable
```python
barrier_disable(volname)
```

Disable Barrier

:param volname: Volume Name
:returns: Output of Barrier command, raises
 GlusterCmdException((rc, out, err)) on error


## profile_start
```python
profile_start(volname)
```

Start Profile

:param volname: Volume Name
:return: Output of Profile command, raises
 GlusterCmdException((rc, out, err)) on error


## profile_stop
```python
profile_stop(volname)
```

Stop Profile

:param volname: Volume Name
:return: Output of Profile command, raises
 GlusterCmdException((rc, out, err)) on error


## profile_info
```python
profile_info(volname, opt, peek=False)
```

Get Profile info

:param volname: Volume Name
:param opt: Operation type of info,
 like peek, incremental, cumulative, clear
:param peek: Use peek or not, default is False
:return: Return profile info, raises
 GlusterCmdException((rc, out, err)) on error

