glustercli-python
==================

This is the official python bindings for `GlusterFS <http://www.gluster.org>`_
CLI.

Hello World
-----------

.. code-block:: python

    from gluster.cli import volume

    # Create a Volume
    volume.create("gv1", ["fvm1:/bricks/b1", "fvm2:/bricks/b2"],
                  force=True)

    # Start Volume
    volume.start("gv1")

    # Read Volume Info
    volume.info("gv1")


.. toctree::
   :glob:

   *
