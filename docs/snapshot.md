
# glustercli.cli.snapshot


## activate
```python
activate(snapname, force=False)
```

Activate Snapshot

:param snapname: Snapshot Name
:param force: True|False Force Activate the snapshot
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## clone
```python
clone(clonename, snapname)
```

Clone the Snapshot

:param clonename: Snapshot Clone Name
:param snapname: Snapshot Name
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## create
```python
create(volname,
       snapname,
       no_timestamp=False,
       description='',
       force=False)
```

Create Snapshot

:param volname: Volume Name
:param snapname: Snapshot Name
:param no_timestamp: True|False Do not add Timestamp to name
:param description: Description for Created Snapshot
:param force: True|False Force Create the snapshot
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## deactivate
```python
deactivate(snapname)
```

Deactivate the Snapshot

:param snapname: Snapshot Name
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## delete
```python
delete(snapname=None, volname=None)
```

Delete Snapshot

:param snapname: Snapshot Name
:param volname: Volume Name
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## info
```python
info(snapname=None, volname=None)
```

Snapshot Info

:param snapname: Snapshot Name
:param volname: Volume Name
:returns: Snapshot Info, raises
 GlusterCmdException((rc, out, err)) on error


## snaplist
```python
snaplist(volname=None)
```

List of Snapshots

:param volname: Volume Name
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## restore
```python
restore(snapname)
```

Restore Snapshot

:param snapname: Snapshot Name
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## status
```python
status(snapname=None, volname=None)
```

Snapshot Status

:param snapname: Snapshot Name
:param volname: Volume Name
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## config
```python
config(volname,
       snap_max_hard_limit=None,
       snap_max_soft_limit=None,
       auto_delete=None,
       activate_on_create=None)
```

Set Snapshot Config

:param volname: Volume Name
:param snap_max_hard_limit: Number of Snapshots hard limit
:param snap_max_soft_limit: Number of Snapshots soft limit
:param auto_delete: True|False Auto delete old snapshots
:param activate_on_create: True|False Activate Snapshot after Create
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error

