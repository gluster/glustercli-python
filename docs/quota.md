
# glustercli.cli.quota


## inode_quota_enable
```python
inode_quota_enable(volname)
```

Enable Inode Quota

:param volname: Volume Name
:returns: Output of inode-quota Enable command, raises
 GlusterCmdException((rc, out, err)) on error


## enable
```python
enable(volname)
```

Enable Quota

:param volname: Volume Name
:returns: Output of quota Enable command, raises
 GlusterCmdException((rc, out, err)) on error


## disable
```python
disable(volname)
```

Disable Inode Quota

:param volname: Volume Name
:returns: Output of quota Disable command, raises
 GlusterCmdException((rc, out, err)) on error


## list_paths
```python
list_paths(volname, paths=[])
```

Get Quota List

:param volname: Volume Name
:param paths: Optional list of paths
:returns: Quota list of paths, raises
 GlusterCmdException((rc, out, err)) on error


## list_objects
```python
list_objects(volname, paths=[])
```

Get Quota Objects List

:param volname: Volume Name
:param paths: Optional list of paths
:returns: Quota list of objects, raises
 GlusterCmdException((rc, out, err)) on error


## remove_path
```python
remove_path(volname, path)
```

Remove Path from Quota list

:param volname: Volume Name
:param path: Path to remove from quota
:returns: Output of Quota remove-path, raises
 GlusterCmdException((rc, out, err)) on error


## remove_objects
```python
remove_objects(volname, path)
```

Remove Objects for a given path

:param volname: Volume Name
:param path: Path to remove from quota
:returns: Output of Quota remove-objects, raises
 GlusterCmdException((rc, out, err)) on error


## default_soft_limit
```python
default_soft_limit(volname, percent)
```

Set default soft limit

:param volname: Volume Name
:param percent: Percent of soft limit
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## limit_usage
```python
limit_usage(volname, path, size, percent=None)
```

Limit quota usage

:param volname: Volume Name
:param path: Path to limit quota
:param size: Limit Size
:param percent: Percentage
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## limit_objects
```python
limit_objects(volname, path, num, percent=None)
```

Limit objects

:param volname: Volume Name
:param path: Path to limit quota
:param num: Limit Number
:param percent: Percentage
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## alert_time
```python
alert_time(volname, a_time)
```

Set Alert Time

:param volname: Volume Name
:param alert_time: Alert Time Value
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## soft_timeout
```python
soft_timeout(volname, timeout)
```

Set Soft Timeout

:param volname: Volume Name
:param timeout: Timeout Value
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## hard_timeout
```python
hard_timeout(volname, timeout)
```

Set Hard Timeout

:param volname: Volume Name
:param timeout: Timeout Value
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error

