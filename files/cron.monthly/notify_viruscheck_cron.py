#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
import re
import traceback

def viruscheck():
    try:
        target_line = [l for l in subprocess.check_output(["/usr/bin/clamdscan" , "/"]).decode('utf-8').splitlines() if re.search("FOUND",l)][-1].replace('\n','').split()
    except subprocess.CalledProcessError:
        traceback.print_exc()
    [subprocess.call(["sudo", "-u#" + str(u) , "DISPLAY=:0", "DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/" + str(u) + "/bus", "/usr/bin/notify-send", target_line[0] + "Virus Found in " + target_line[1] ]) for u in range(1000, 1003)]


if __name__ == "__main__":
    viruscheck()