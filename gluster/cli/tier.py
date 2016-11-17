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

from .utils import tier_execute, tier_execute_xml
from .parsers import parse_tier_detach, parse_tier_status


def status(volname):
    """
    Tier Status

    :param volname: Volume Name
    :returns: Output of the command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = [volname, "status"]
    return parse_tier_status(tier_execute_xml(cmd))


def start(volname, force=False):
    """
    Start Tier

    :param volname: Volume Name
    :returns: Output of the command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = [volname, "start"]
    if force:
        cmd += ["force"]

    return tier_execute(cmd)


def attach(volname, bricks, replica=None):
    """
    Attach Tier

    :param volname: Volume Name
    :param bricks: Tier Bricks to attach
    :param replica: Replica number
    :returns: Output of the command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = [volname, "attach"]
    if replica is not None:
        cmd += ["replica", "{0}".format(replica)]

    cmd += bricks

    return tier_execute(cmd)


def detach_start(volname, bricks, force=False):
    """
    Detach Tier Start

    :param volname: Volume Name
    :param bricks: Tier Bricks to detach
    :param force: True|False Force Detach the Tier
    :returns: Output of the command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = [volname, "detach", bricks, "start"]

    if force:
        cmd += ["force"]

    return tier_execute(cmd)


def detach_stop(volname, bricks, force=False):
    """
    Detach Tier Stop

    :param volname: Volume Name
    :param bricks: Tier Bricks to detach
    :param force: True|False Force Detach the Tier
    :returns: Output of the command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = [volname, "detach", bricks, "stop"]

    if force:
        cmd += ["force"]

    return tier_execute(cmd)


def detach_commit(volname, bricks, force=False):
    """
    Detach Tier Commit

    :param volname: Volume Name
    :param bricks: Tier Bricks to detach
    :param force: True|False Force Detach the Tier
    :returns: Output of the command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = [volname, "detach", bricks, "commit"]

    if force:
        cmd += ["force"]

    return tier_execute(cmd)


def detach_status(volname, bricks, force=False):
    """
    Detach Tier Status

    :param volname: Volume Name
    :param bricks: Tier Bricks to attach
    :param force: True|False Force Detach the Tier
    :returns: Output of the command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = [volname, "detach", bricks, "status"]

    if force:
        cmd += ["force"]

    return parse_tier_detach(tier_execute_xml(cmd))
