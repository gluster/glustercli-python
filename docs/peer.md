
# glustercli.cli.peer


## probe
```python
probe(host)
```

Add Host to Cluster

:param host: Hostname or IP
:returns: Output of peer probe command, raises
 GlusterCmdException((rc, out, err)) on error


## attach
```python
attach(host)
```

Add Host to Cluster, alias for probe

:param host: Hostname or IP
:returns: Output of peer probe command, raises
 GlusterCmdException((rc, out, err)) on error


## detach
```python
detach(host)
```

Remove Host from Cluster

:param host: Hostname or IP
:returns: Output of peer detach command, raises
 GlusterCmdException((rc, out, err)) on error


## detach_all
```python
detach_all()
```

Removes All Hosts from Cluster

:returns: Output of peer detach command, raises
 GlusterCmdException((rc, out, err)) on error


## status
```python
status()
```

Peer Status of Cluster

:returns: Output of peer status command, raises
 GlusterCmdException((rc, out, err)) on error


## pool
```python
pool()
```

Cluster Pool Status

:returns: Pool list and status, raises
 GlusterCmdException((rc, out, err)) on error

