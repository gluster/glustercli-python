docgen:
	pydocmd simple glustercli.cli.volume++ > docs/volume.md
	pydocmd simple glustercli.cli.bitrot++ > docs/bitrot.md
	pydocmd simple glustercli.cli.bricks++ > docs/bricks.md
	pydocmd simple glustercli.cli.georep++ > docs/georep.md
	pydocmd simple glustercli.cli.peer++ > docs/peer.md
	pydocmd simple glustercli.cli.quota++ > docs/quota.md
	pydocmd simple glustercli.cli.snapshot++ > docs/snapshot.md
	pydocmd simple glustercli.cli.heal++ > docs/heal.md
	pydocmd simple glustercli.cli.nfs_ganesha++ > docs/nfs_ganesha.md
	pydocmd simple glustercli.cli.rebalance++ > docs/rebalance.md
	pydocmd simple glustercli.cli.set_gluster_path > docs/utils.md
	pydocmd simple glustercli.cli.set_gluster_socket >> docs/utils.md
	pydocmd simple glustercli.cli.set_ssh_host >> docs/utils.md
	pydocmd simple glustercli.cli.set_ssh_pem_file >> docs/utils.md
	pydocmd simple glustercli.cli.ssh_connection >> docs/utils.md
	pydocmd simple glustercli.cli.GlusterCmdException >> docs/utils.md

	pydocmd simple glustercli.metrics.local_processes++ > docs/local_processes.md
	pydocmd simple glustercli.metrics.local_utilization++ > docs/local_utilization.md
	pydocmd simple glustercli.metrics.local_diskstats++ > docs/local_diskstats.md
