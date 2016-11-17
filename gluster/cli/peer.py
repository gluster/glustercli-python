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

from .utils import peer_execute, peer_execute_xml, gluster_execute_xml
from .parsers import parse_peer_status, parse_pool_list


def probe(host):
    """
    Add Host to Cluster

    :param host: Hostname or IP
    :returns: Output of peer probe command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["probe", host]
    return peer_execute(cmd)


def attach(host):
    """
    Add Host to Cluster, alias for probe

    :param host: Hostname or IP
    :returns: Output of peer probe command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    return probe(host)


def detach(host):
    """
    Remove Host from Cluster

    :param host: Hostname or IP
    :returns: Output of peer detach command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["detach", host]
    return peer_execute(cmd)


def status():
    """
    Peer Status of Cluster

    :returns: Output of peer status command, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["status"]
    return parse_peer_status(peer_execute_xml(cmd))


def pool():
    """
    Cluster Pool Status

    :returns: Pool list and status, raises
     GlusterCmdException((rc, out, err)) on error
    """
    cmd = ["pool", "list"]
    return parse_pool_list(gluster_execute_xml(cmd))
