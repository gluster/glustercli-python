
# glustercli.cli.rebalance


## fix_layout_start
```python
fix_layout_start(volname)
```

Fix Layout Rebalance Start

:param volname: Volume Name
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## start
```python
start(volname, force=False)
```

Rebalance Start

:param volname: Volume Name
:param force: True|False Force start the rebalance
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## stop
```python
stop(volname)
```

Rebalance Stop

:param volname: Volume Name
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## status
```python
status(volname)
```

Rebalance Status

:param volname: Volume Name
:returns: Rebalance Status, raises
 GlusterCmdException((rc, out, err)) on error

