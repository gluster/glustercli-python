
# glustercli.cli.bitrot


## enable
```python
enable(volname)
```

Enable Bitrot Feature

:param volname: Volume Name
:returns: Output of Enable command, raises
 GlusterCmdException((rc, out, err)) on error


## disable
```python
disable(volname)
```

Disable Bitrot Feature

:param volname: Volume Name
:returns: Output of Disable command, raises
 GlusterCmdException((rc, out, err)) on error


## scrub_throttle
```python
scrub_throttle(volname, throttle_type)
```

Configure Scrub Throttle

:param volname: Volume Name
:param throttle_type: lazy|normal|aggressive
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## scrub_frequency
```python
scrub_frequency(volname, freq)
```

Configure Scrub Frequency

:param volname: Volume Name
:param freq: hourly|daily|weekly|biweekly|monthly
:returns: Output of the command, raises
 GlusterCmdException((rc, out, err)) on error


## scrub_pause
```python
scrub_pause(volname)
```

Pause Bitrot Scrub

:param volname: Volume Name
:returns: Output of Pause command, raises
 GlusterCmdException((rc, out, err)) on error


## scrub_resume
```python
scrub_resume(volname)
```

Resume Bitrot Scrub

:param volname: Volume Name
:returns: Output of the Resume command, raises
 GlusterCmdException((rc, out, err)) on error


## scrub_status
```python
scrub_status(volname)
```

Scrub Status

:param volname: Volume Name
:returns: Scrub Status, raises
 GlusterCmdException((rc, out, err)) on error

