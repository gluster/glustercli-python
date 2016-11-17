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
from .utils import bitrot_execute, bitrot_execute_xml, GlusterCmdException
from .parsers import parse_bitrot_scrub_status

THROTTLE_TYPES = ["lazy", "normal", "aggressive"]
FREQUENCY_TYPES = ["hourly", "daily", "weekly", "biweekly", "monthly"]


def enable(volname):
    """
    Enable Bitrot Feature

    :param volname: Volume Name
    :returns: Output of Enable command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = [volname, "enable"]
    return bitrot_execute(cmd)


def disable(volname):
    """
    Disable Bitrot Feature

    :param volname: Volume Name
    :returns: Output of Disable command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = [volname, "disable"]
    return bitrot_execute(cmd)


def scrub_throttle(volname, throttle_type):
    """
    Configure Scrub Throttle

    :param volname: Volume Name
    :param throttle_type: lazy|normal|aggressive
    :returns: Output of the command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    if throttle_type.lower() not in THROTTLE_TYPES:
        raise GlusterCmdException((-1, "", "Invalid Scrub Throttle Type"))
    cmd = [volname, "scrub-throttle", throttle_type.lower()]
    return bitrot_execute(cmd)


def scrub_frequency(volname, freq):
    """
    Configure Scrub Frequency

    :param volname: Volume Name
    :param freq: hourly|daily|weekly|biweekly|monthly
    :returns: Output of the command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    if freq.lower() not in FREQUENCY_TYPES:
        raise GlusterCmdException((-1, "", "Invalid Scrub Frequency"))
    cmd = [volname, "scrub-frequency", freq]
    return bitrot_execute(cmd)


def scrub_pause(volname):
    """
    Pause Bitrot Scrub

    :param volname: Volume Name
    :returns: Output of Pause command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = [volname, "scrub", "pause"]
    return bitrot_execute(cmd)


def scrub_resume(volname):
    """
    Resume Bitrot Scrub

    :param volname: Volume Name
    :returns: Output of the Resume command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = [volname, "scrub", "resume"]
    return bitrot_execute(cmd)


def scrub_status(volname):
    """
    Scrub Status

    :param volname: Volume Name
    :returns: Scrub Status, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = [volname, "scrub", "status"]
    return parse_bitrot_scrub_status(bitrot_execute_xml(cmd))
