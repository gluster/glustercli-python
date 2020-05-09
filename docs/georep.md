
# glustercli.cli.georep


## gsec_create
```python
gsec_create(ssh_key_prefix=True)
```

Generate Geo-replication SSH Keys

:param ssh_key_prefix: True|False Command prefix in generated public keys
:returns: Output of gsec_create command, raises
 GlusterCmdException((rc, out, err)) on error


## create
```python
create(volname,
       slave_host,
       slave_vol,
       slave_user='root',
       push_pem=True,
       no_verify=False,
       force=False,
       ssh_port=22)
```

Create Geo-replication Session

:param volname: Master Volume Name
:param slave_host: Slave Hostname or IP
:param slave_vol: Slave Volume
:param slave_user: Slave User, default is "root"
:param push_pem: True|False Push SSH keys to Slave
:param no_verify: True|False Skip the Slave Verification
 process before create
:param force: True|False Force Create Session
:param ssh_port: SSH Port, Default is 22
:returns: Output of Create command, raises
 GlusterCmdException((rc, out, err)) on error


## start
```python
start(volname, slave_host, slave_vol, slave_user='root', force=False)
```

Start Geo-replication Session

:param volname: Master Volume Name
:param slave_host: Slave Hostname or IP
:param slave_vol: Slave Volume
:param slave_user: Slave User, default is "root"
:param force: True|False Force Start the Session
:returns: Output of Start command, raises
 GlusterCmdException((rc, out, err)) on error


## stop
```python
stop(volname, slave_host, slave_vol, slave_user='root', force=False)
```

Stop Geo-replication Session

:param volname: Master Volume Name
:param slave_host: Slave Hostname or IP
:param slave_vol: Slave Volume
:param slave_user: Slave User, default is "root"
:param force: True|False Force Stop the Session
:returns: Output of Stop command, raises
 GlusterCmdException((rc, out, err)) on error


## restart
```python
restart(volname, slave_host, slave_vol, slave_user='root', force=False)
```

Restart Geo-replication Session

:param volname: Master Volume Name
:param slave_host: Slave Hostname or IP
:param slave_vol: Slave Volume
:param slave_user: Slave User, default is "root"
:param force: True|False Force Start the Session
:returns: Output of Start command, raises
 GlusterCmdException((rc, out, err)) on error


## delete
```python
delete(volname,
       slave_host,
       slave_vol,
       slave_user='root',
       reset_sync_time=None)
```

Delete Geo-replication Session

:param volname: Master Volume Name
:param slave_host: Slave Hostname or IP
:param slave_vol: Slave Volume
:param slave_user: Slave User, default is "root"
:param reset_sync_time: True|False Reset Sync time on delete
:returns: Output of Start command, raises
 GlusterCmdException((rc, out, err)) on error


## pause
```python
pause(volname, slave_host, slave_vol, slave_user='root', force=False)
```

Pause Geo-replication Session

:param volname: Master Volume Name
:param slave_host: Slave Hostname or IP
:param slave_vol: Slave Volume
:param slave_user: Slave User, default is "root"
:param force: True|False Force Pause Session
:returns: Output of Pause command, raises
 GlusterCmdException((rc, out, err)) on error


## resume
```python
resume(volname, slave_host, slave_vol, slave_user='root', force=False)
```

Resume Geo-replication Session

:param volname: Master Volume Name
:param slave_host: Slave Hostname or IP
:param slave_vol: Slave Volume
:param slave_user: Slave User, default is "root"
:param force: True|False Force Resume Session
:returns: Output of Resume command, raises
 GlusterCmdException((rc, out, err)) on error


## config_set
```python
config_set(volname,
           slave_host,
           slave_vol,
           key,
           value,
           slave_user='root')
```

Set Config of a Geo-replication Session

:param volname: Master Volume Name
:param slave_host: Slave Hostname or IP
:param slave_vol: Slave Volume
:param slave_user: Slave User, default is "root"
:param key: Config Key
:param value: Config Value
:returns: Output of Config set command, raises
 GlusterCmdException((rc, out, err)) on error


## config_reset
```python
config_reset(volname, slave_host, slave_vol, key, slave_user='root')
```

Reset configuration of Geo-replication Session

:param volname: Master Volume Name
:param slave_host: Slave Hostname or IP
:param slave_vol: Slave Volume
:param slave_user: Slave User, default is "root"
:param key: Config Key
:returns: Output of Config reset command, raises
 GlusterCmdException((rc, out, err)) on error


## config_get
```python
config_get(volname, slave_host, slave_vol, key=None, slave_user='root')
```

Get Configuration of Geo-replication Session

:param volname: Master Volume Name
:param slave_host: Slave Hostname or IP
:param slave_vol: Slave Volume
:param slave_user: Slave User, default is "root"
:param key: Config Key
:returns: Geo-rep session Config Values, raises
 GlusterCmdException((rc, out, err)) on error


## status
```python
status(volname=None, slave_host=None, slave_vol=None, slave_user='root')
```

Status of Geo-replication Session

:param volname: Master Volume Name
:param slave_host: Slave Hostname or IP
:param slave_vol: Slave Volume
:param slave_user: Slave User, default is "root"
:returns: Geo-replication Status, raises
 GlusterCmdException((rc, out, err)) on error

