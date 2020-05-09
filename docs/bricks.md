
# glustercli.cli.bricks


## add
```python
add(volname,
    bricks,
    stripe=None,
    replica=None,
    arbiter=None,
    force=False)
```

Add Bricks

:param volname: Volume Name
:param bricks: List of Bricks
:param stripe: Stripe Count
:param replica: Replica Count
:param arbiter: Arbiter Count
:param force: True|False Force Add Bricks
:returns: Output of add-brick command, raises
 GlusterCmdException((rc, out, err)) on error


## remove_start
```python
remove_start(volname, bricks, replica=None, force=False)
```

Remove Bricks start

:param volname: Volume Name
:param bricks: List of Bricks
:param replica: Replica Count
:param force: True|False Force Remove Bricks
:returns: Output of remove-brick start command, raises
 GlusterCmdException((rc, out, err)) on error


## remove_stop
```python
remove_stop(volname, bricks, replica=None, force=False)
```

Remove Bricks stop

:param volname: Volume Name
:param bricks: List of Bricks
:param replica: Replica Count
:param force: True|False Force Remove Bricks
:returns: Output of remove-brick stop command, raises
 GlusterCmdException((rc, out, err)) on error


## remove_commit
```python
remove_commit(volname, bricks, replica=None, force=False)
```

Remove Bricks Commit

:param volname: Volume Name
:param bricks: List of Bricks
:param replica: Replica Count
:param force: True|False Force Remove Bricks
:returns: Output of remove-brick commit command, raises
 GlusterCmdException((rc, out, err)) on error


## remove_status
```python
remove_status(volname, bricks, replica=None, force=False)
```

Remove Bricks status

:param volname: Volume Name
:param bricks: List of Bricks
:param replica: Replica Count
:param force: True|False Force Remove Bricks
:returns: Remove Bricks Status, raises
 GlusterCmdException((rc, out, err)) on error


## replace_commit
```python
replace_commit(volname, source_brick, new_brick, force=False)
```

Replace Bricks

:param volname: Volume Name
:param source_brick: Source Brick
:param new_brick: New Replacement Brick
:param force: True|False Force Replace Bricks
:returns: Output of replace-brick command, raises
 GlusterCmdException((rc, out, err)) on error

