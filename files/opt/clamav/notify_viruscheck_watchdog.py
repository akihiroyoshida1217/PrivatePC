#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import signal
import subprocess
import re
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from systemd.daemon import notify


class MyHandler(PatternMatchingEventHandler):
    def __init__(self, path, patterns):
        super(MyHandler, self).__init__(patterns=patterns)
        self.path = path

    def _run_command(self):
        try:
            ld = open("/var/log/clamav/clamav.log")
            #ld = open(path)
            lines = ld.readlines()
            ld.close()

            target_line_num = [i for i, line in enumerate(lines) if re.search("Started at",line)][-1]

            target_line = [l for l in lines[target_line_num:] if re.search("FOUND",l)][-1].replace('\n','').split()

            [subprocess.call(["sudo", "-u#" + str(u) , "DISPLAY=:0", "DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/" + str(u) + "/bus", "/usr/bin/notify-send", target_line[7] + " Virus Found in " + target_line[6] ]) for u in range(1000, 1003)]
        except:
            None

    def on_moved(self, event):
        self._run_command()

    def on_created(self, event):
        self._run_command()

    def on_deleted(self, event):
        self._run_command()

    def on_modified(self, event):
        self._run_command()

def termed(signum, frame):
    sys.exit(0)

def watch(path, patterns):
    signal.signal(signal.SIGTERM, termed)
    event_handler = MyHandler(path, patterns)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            #notify(Notification.STATUS, "I'm fine.")
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    finally:
        observer.stop()
        notify("STOPPING=1")
    observer.join()

if __name__ == "__main__":
    notify("READY=1")
    watch("/var/log/clamav/", "clamav.log*")
