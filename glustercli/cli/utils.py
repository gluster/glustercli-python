# -*- coding: utf-8 -*-

import subprocess
from contextlib import contextmanager

GLUSTERCMD = "gluster"
GLUSTERD_SOCKET = None
ssh = None
SSH_HOST = None
SSH_PEM_FILE = None
prev_ssh_host = None
prev_ssh_pem_file = None


@contextmanager
def ssh_connection(hostname, pem_file):
    global SSH_HOST, SSH_PEM_FILE
    SSH_HOST = hostname
    SSH_PEM_FILE = pem_file
    yield
    SSH_HOST = None
    SSH_PEM_FILE = None


def execute(cmd):
    global prev_ssh_host, prev_ssh_pem_file

    cmd_args = []
    cmd_args.append(GLUSTERCMD)

    if GLUSTERD_SOCKET:
        cmd_args.append("--glusterd-sock={0}".format(GLUSTERD_SOCKET))

    cmd_args.append("--mode=script")
    cmd_args += cmd

    if SSH_HOST is not None and SSH_PEM_FILE is not None:
        # Reconnect only if first time or previously connected to different
        # host or using different pem key
        if ssh is None or prev_ssh_host != SSH_HOST \
           or prev_ssh_pem_file != SSH_PEM_FILE:
            __connect_ssh()
            prev_ssh_host = SSH_HOST
            prev_ssh_pem_file = SSH_PEM_FILE

        cmd_args = " ".join(cmd_args)
        _, stdout, stderr = ssh.exec_command(cmd_args)
        returncode = stdout.channel.recv_exit_status()
        return (returncode, stdout.read().strip(), stderr.read().strip())

    proc = subprocess.Popen(cmd_args, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True)
    out, err = proc.communicate()
    return (proc.returncode, out, err)


class GlusterCmdException(Exception):
    pass


def set_ssh_pem_file(pem_file):
    global USE_SSH, SSH_PEM_FILE
    USE_SSH = True
    SSH_PEM_FILE = pem_file


def set_ssh_host(hostname):
    global SSH_HOST
    SSH_HOST = hostname


def __connect_ssh():
    global ssh

    import paramiko  # noqa # pylint: disable=import-outside-toplevel

    if ssh is None:
        ssh = paramiko.SSHClient()
        try:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(SSH_HOST, username="root", key_filename=SSH_PEM_FILE)
        except paramiko.ssh_exception.AuthenticationException as err:
            raise GlusterCmdException("Unable to establish SSH connection "
                                      "to root@{0}:\n{1}".format(
                                          SSH_HOST, err))


def set_gluster_path(path):
    global GLUSTERCMD
    GLUSTERCMD = path


def set_gluster_socket(path):
    global GLUSTERD_SOCKET
    GLUSTERD_SOCKET = path


def execute_or_raise(cmd):
    returncode, out, err = execute(cmd)
    if returncode != 0:
        raise GlusterCmdException((returncode, out, err))

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
