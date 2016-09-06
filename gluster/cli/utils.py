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


def execute(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return p.returncode, out, err


class GlusterCmdException(Exception):
    pass


def set_gluster_path(path):
    global GLUSTERCMD
    GLUSTERCMD = path


def execute_or_raise(cmd):
    rc, out, err = execute(cmd)
    if rc != 0:
        raise GlusterCmdException((rc, out, err))

    return out.strip()


def gluster_system_execute(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "system::", "execute"] + cmd
    return execute_or_raise(cmd)


def gluster_execute(cmd):
    cmd = [GLUSTERCMD, "--mode=script"] + cmd
    return execute_or_raise(cmd)


def gluster_execute_xml(cmd):
    cmd = [GLUSTERCMD, "--mode=script"] + cmd + ["--xml"]
    return execute_or_raise(cmd)


def volume_execute(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "volume"] + cmd
    return execute_or_raise(cmd)


def peer_execute(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "peer"] + cmd
    return execute_or_raise(cmd)


def volume_execute_xml(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "volume"] + cmd + ["--xml"]
    return execute_or_raise(cmd)


def peer_execute_xml(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "peer"] + cmd + ["--xml"]
    return execute_or_raise(cmd)


def georep_execute(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "volume", "geo-replication"] + cmd
    return execute_or_raise(cmd)


def georep_execute_xml(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "volume", "geo-replication"] + cmd + [
        "--xml"]
    return execute_or_raise(cmd)


def bitrot_execute(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "volume", "bitrot"] + cmd
    return execute_or_raise(cmd)


def bitrot_execute_xml(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "volume", "bitrot"] + cmd + ["--xml"]
    return execute_or_raise(cmd)


def quota_execute(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "volume", "quota"] + cmd
    return execute_or_raise(cmd)


def quota_execute_xml(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "volume", "quota"] + cmd + ["--xml"]
    return execute_or_raise(cmd)


def heal_execute(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "volume", "heal"] + cmd
    return execute_or_raise(cmd)


def heal_execute_xml(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "volume", "heal"] + cmd + ["--xml"]
    return execute_or_raise(cmd)


def snapshot_execute(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "snapshot"] + cmd
    return execute_or_raise(cmd)


def snapshot_execute_xml(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "snapshot"] + cmd + ["--xml"]
    return execute_or_raise(cmd)


def tier_execute(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "volume", "tier"] + cmd
    return execute_or_raise(cmd)


def tier_execute_xml(cmd):
    cmd = [GLUSTERCMD, "--mode=script", "volume", "tier"] + cmd + ["--xml"]
    return execute_or_raise(cmd)
