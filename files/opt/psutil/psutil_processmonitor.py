#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil
import subprocess
from systemd.daemon import notify

def process_monitor(target_process):
    try:
        while True:
            abort_process = [[ t for t in target_process if t not in p ] for p in psutil.process_iter(attrs=["cmdline"]) ]
            if not abort_process:
                [subprocess.call(["sudo", "-u#" + str(u) , "DISPLAY=:0", "DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/" + str(u) + "/bus", "/usr/bin/notify-send", "Process " + ",".join(abort_process)) + " is aborted!" ]) for u in range(1000, 1003)]
            else:
                None
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    finally:
        observer.stop()
        notify("STOPPING=1")

if __name__ == "__main__":
    notify("READY=1")
    process_monitor(["/sbin/auditd","/usr/sbin/clamd","/opt/clamav/notify_viruscheck_watchdog.py","/opt/etc_watchdog/etc_watchdog.py"])
