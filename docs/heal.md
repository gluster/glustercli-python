
# glustercli.cli.heal


## enable
```python
enable(volname)
```

Enable Volume Heal

:param volname: Volume Name
:returns: Output of Enable command, raises
 GlusterCmdException((rc, out, err)) on error


## disable
```python
disable(volname)
```

Disable Volume Heal

:param volname: Volume Name
:returns: Output of Disable command, raises
 GlusterCmdException((rc, out, err)) on error


## full
```python
full(volname)
```

Full Volume Heal

:param volname: Volume Name
:returns: Output of Full Heal command, raises
 GlusterCmdException((rc, out, err)) on error


## statistics
```python
statistics(volname)
```

Get Statistics of Heal

:param volname: Volume Name
:returns: Output of Statistics command, raises
 GlusterCmdException((rc, out, err)) on error


## info
```python
info(volname, info_type=None)
```

Get Volume Heal Info

:param volname: Volume Name
:returns: Output of Heal Info command, raises
 GlusterCmdException((rc, out, err)) on error


## split_brain
```python
split_brain(volname,
            bigger_file=None,
            latest_mtime=None,
            source_brick=None,
            path=None)
```

Split Brain Resolution

:param volname: Volume Name
:param bigger_file: File Path of Bigger file
:param latest_mtime: File Path of Latest mtime
:param source_brick: Source Brick for Good Copy
:param path: Resolution of this path/file
:returns: Output of Split-brain command, raises
 GlusterCmdException((rc, out, err)) on error

