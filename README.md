# glustercli-python

Python bindings for [GlusterFS](http://www.gluster.org) CLI and Metrics.

## Hello World

```python
from glustercli.cli import volume

# Create a Volume
volume.create("gv1", ["fvm1:/bricks/b1", "fvm2:/bricks/b2"],
              force=True)

# Start Volume
volume.start("gv1")

# Read Volume Info
volume.info("gv1")

# Get GlusterFS version
from glustercli.cli import glusterfs_version
print(glusterfs_version())
```

## Install

```
sudo pip3 install glustercli
```

## Documentation

See [Documentation](docs/README.md)

Install `pydoc-markdown` package to generate Documentation.

```
sudo pip3 install pydoc-markdown
```
