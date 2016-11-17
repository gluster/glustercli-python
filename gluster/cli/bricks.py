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
from .utils import volume_execute, volume_execute_xml
from .parsers import parse_remove_brick_status


def add(volname, bricks, stripe=None, replica=None, arbiter=None, force=False):
    """
    Add Bricks

    :param volname: Volume Name
    :param bricks: List of Bricks
    :param stripe: Stripe Count
    :param replica: Replica Count
    :param arbiter: Arbiter Count
    :param force: True|False Force Add Bricks
    :returns: Output of add-brick command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["add-brick", volname]
    if stripe is not None:
        cmd += ["stripe", "{0}".format(stripe)]

    if replica is not None:
        cmd += ["replica", "{0}".format(replica)]

    if arbiter is not None:
        cmd += ["arbiter", "{0}".format(arbiter)]

    cmd += bricks

    if force:
        cmd += ["force"]

    return volume_execute(cmd)


def remove_start(volname, bricks, replica=None, force=False):
    """
    Remove Bricks start

    :param volname: Volume Name
    :param bricks: List of Bricks
    :param replica: Replica Count
    :param force: True|False Force Remove Bricks
    :returns: Output of remove-brick start command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["remove-brick", volname]
    if replica is not None:
        cmd += ["replica", "{0}".format(replica)]

    cmd += bricks
    cmd += ["start"]
    if force:
        cmd += ["force"]

    return volume_execute(cmd)


def remove_stop(volname, bricks, replica=None, force=False):
    """
    Remove Bricks stop

    :param volname: Volume Name
    :param bricks: List of Bricks
    :param replica: Replica Count
    :param force: True|False Force Remove Bricks
    :returns: Output of remove-brick stop command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["remove-brick", volname]
    if replica is not None:
        cmd += ["replica", "{0}".format(replica)]

    cmd += bricks
    cmd += ["stop"]
    if force:
        cmd += ["force"]

    return volume_execute(cmd)


def remove_commit(volname, bricks, replica=None, force=False):
    """
    Remove Bricks Commit

    :param volname: Volume Name
    :param bricks: List of Bricks
    :param replica: Replica Count
    :param force: True|False Force Remove Bricks
    :returns: Output of remove-brick commit command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["remove-brick", volname]
    if replica is not None:
        cmd += ["replica", "{0}".format(replica)]

    cmd += bricks
    cmd += ["commit"]
    if force:
        cmd += ["force"]

    return volume_execute(cmd)


def remove_status(volname, bricks, replica=None, force=False):
    """
    Remove Bricks status

    :param volname: Volume Name
    :param bricks: List of Bricks
    :param replica: Replica Count
    :param force: True|False Force Remove Bricks
    :returns: Remove Bricks Status, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["remove-brick", volname]
    if replica is not None:
        cmd += ["replica", "{0}".format(replica)]

    cmd += bricks
    cmd += ["status"]
    if force:
        cmd += ["force"]

    return parse_remove_brick_status(volume_execute_xml(cmd))


def replace_commit(volname, source_brick, new_brick, force=False):
    """
    Replace Bricks

    :param volname: Volume Name
    :param source_brick: Source Brick
    :param new_brick: New Replacement Brick
    :param force: True|False Force Replace Bricks
    :returns: Output of replace-brick command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["replace-brick", volname, source_brick, new_brick, "commit"]
    if force:
        cmd += ["force"]
    return volume_execute(cmd)
