# -*- coding: utf-8 -*-
#
#  Copyright (c) 2016 Red Hat, Inc. <http://www.redhat.com>
#  This file is part of GlusterFS.
#
#  This file is licensed to you under your choice of the GNU Lesser
#  General Public License, version 3 or any later version (LGPLv3 or
#  later), or the GNU General Public License, version 2 (GPLv2), in all
#  cases as published by the Free Software Foundation.
#
from .utils import gluster_execute


def enable():
    """
    Enable NFS Ganesha

    :returns: Output of Enable command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["nfs-ganesha", "enable"]
    return gluster_execute(cmd)


def disable():
    """
    Disable NFS Ganesha

    :returns: Output of Disable command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["nfs-ganesha", "disable"]
    return gluster_execute(cmd)
