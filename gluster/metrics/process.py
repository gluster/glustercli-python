import subprocess

import cmdlineparser

GLUSTER_PROCS = [
    "glusterd",
    "glusterfsd",
    "glustershd",
    "glusterfs",
    "python",  # gsyncd, glustereventsd etc
    "ssh",  # gsyncd related ssh connections
]


def get_cmdline(pid):
    args = []
    try:
        with open("/proc/{0}/cmdline".format(pid), "r") as f:
            args = f.read().strip("\x00").split("\x00")
    except IOError:
        pass

    return args


def local_processes():
    # Run ps command and get all the details for all gluster processes
    # ps --no-header -ww -o pid,pcpu,pmem,rsz,vsz,comm -C glusterd,glusterfsd
    # command can be used instead of comm, but if an argument has space then
    # it is a problem
    # for example `mytool "hello world" arg2` will be displayed as
    # `mytool hello world arg2` in ps output
    # Read cmdline from `/proc/<pid>/cmdline` to get full commands
    # Use argparse to parse the output and form the key
    # Example output of ps command:
    # 1406  0.0  0.5 11176 805048 glusterfsd
    # 1416  0.0  0.5 11208 805048 glusterfsd
    details = []
    cmd = ["ps",
           "--no-header",  # No header in the output
           "-ww",  # To set unlimited width to avoid crop
           "-o",  # Output Format
           "pid,pcpu,pmem,rsz,vsz,comm",
           "-C",
           ",".join(GLUSTER_PROCS)]

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = p.communicate()
    # No records in `ps` output
    if p.returncode != 0:
        return details

    data = out.strip()

    for line in data.split("\n"):
        # Sample data:
        # 1406  0.0  0.5 11176 805048 glusterfsd
        pid, pcpu, pmem, rsz, vsz, comm = line.strip().split()

        args = get_cmdline(int(pid))
        if not args:
            # Unable to collect the cmdline, may be IO error and process died?
            continue

        cmdname = args[0].split("/")[-1]
        func_name = "parse_cmdline_" + cmdname
        details_func = getattr(cmdlineparser, func_name, None)

        if details_func is not None:
            data = details_func(args)
            if data is not None:
                data["percentage_cpu"] = float(pcpu)
                data["percentage_memory"] = float(pmem)
                data["resident_memory"] = int(rsz)
                data["virtual_memory"] = int(vsz)
                data["pid"] = int(pid)
                details.append(data)

    return details
