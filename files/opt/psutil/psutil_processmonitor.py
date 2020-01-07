#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil
import subprocess

def process_monitor(processes):
    while True:
        abort_process = set(processes) - set(psutil.process_iter(attrs=["name"]))
        if abort_process != set():
            [subprocess.call(["sudo", "-u#" + str(u) , "DISPLAY=:0", "DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/" + str(u) + "/bus", "/usr/bin/notify-send", "Process " + ",".join(list(abort_process)) + " is aborted!" ]) for u in range(1000, 1003)]
        else:
            None
        time.sleep(1)

if __name__ == "__main__":
    process_monitor(["/sbin/auditd","/usr/sbin/clamd","inotify_watchdog.py"])
