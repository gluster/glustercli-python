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

import subprocess

GLUSTERCMD = "gluster"
GLUSTERD_SOCKET = None


def execute(cmd):
    c = []
    c.append(GLUSTERCMD)

    if GLUSTERD_SOCKET:
        c.append("--glusterd-sock={0}".format(GLUSTERD_SOCKET))

    c.append("--mode=script")
    c += cmd

    p = subprocess.Popen(c, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return p.returncode, out, err


class GlusterCmdException(Exception):
    pass


def set_gluster_path(path):
    global GLUSTERCMD
    GLUSTERCMD = path


def set_gluster_socket(path):
    global GLUSTERD_SOCKET
    GLUSTERD_SOCKET = path


def execute_or_raise(cmd):
    rc, out, err = execute(cmd)
    if rc != 0:
        raise GlusterCmdException((rc, out, err))

    return out.strip()


def gluster_system_execute(cmd):
    cmd.insert(0, "system::")
    cmd.insert(1, "execute")
    return execute_or_raise(cmd)


def gluster_execute(cmd):
    return execute_or_raise(cmd)


def gluster_execute_xml(cmd):
    cmd.append("--xml")
    return execute_or_raise(cmd)


def volume_execute(cmd):
    cmd.insert(0, "volume")
    return execute_or_raise(cmd)


def peer_execute(cmd):
    cmd.insert(0, "peer")
    return execute_or_raise(cmd)


def volume_execute_xml(cmd):
    cmd.insert(0, "volume")
    return gluster_execute_xml(cmd)


def peer_execute_xml(cmd):
    cmd.insert(0, "peer")
    return gluster_execute_xml(cmd)


def georep_execute(cmd):
    cmd.insert(0, "volume")
    cmd.insert(1, "geo-replication")
    return execute_or_raise(cmd)


def georep_execute_xml(cmd):
    cmd.insert(0, "volume")
    cmd.insert(1, "geo-replication")
    return gluster_execute_xml(cmd)


def bitrot_execute(cmd):
    cmd.insert(0, "volume")
    cmd.insert(1, "bitrot")
    return execute_or_raise(cmd)


def bitrot_execute_xml(cmd):
    cmd.insert(0, "volume")
    cmd.insert(1, "bitrot")
    return gluster_execute_xml(cmd)


def quota_execute(cmd):
    cmd.insert(0, "volume")
    cmd.insert(1, "quota")
    return execute_or_raise(cmd)


def quota_execute_xml(cmd):
    cmd.insert(0, "volume")
    cmd.insert(1, "quota")
    return gluster_execute_xml(cmd)


def heal_execute(cmd):
    cmd.insert(0, "volume")
    cmd.insert(1, "heal")
    return execute_or_raise(cmd)


def heal_execute_xml(cmd):
    cmd.insert(0, "volume")
    cmd.insert(1, "heal")
    return gluster_execute_xml(cmd)


def snapshot_execute(cmd):
    cmd.insert(0, "snapshot")
    return execute_or_raise(cmd)


def snapshot_execute_xml(cmd):
    cmd.insert(0, "snapshot")
    return gluster_execute_xml(cmd)


def tier_execute(cmd):
    cmd.insert(0, "volume")
    cmd.insert(1, "tier")
    return execute_or_raise(cmd)


def tier_execute_xml(cmd):
    cmd.insert(0, "volume")
    cmd.insert(1, "tier")
    return gluster_execute_xml(cmd)
