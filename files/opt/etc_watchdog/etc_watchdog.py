#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import signal
import subprocess
import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from systemd.daemon import notify


class MyHandler(FileSystemEventHandler):
    def _run_command(self, event):
        try:
            [subprocess.call(["sudo", "-u#" + str(u) , "DISPLAY=:0", "DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/" + str(u) + "/bus", "/usr/bin/notify-send", "Falsify Found in " + event.src_path+ " ,Type is " + target_line[4] ]) for u in range(1000, 1003)]
        except:
            None

    def on_moved(self, event):
        self._run_command(event)

    def on_created(self, event):
        self._run_command(event)

    def on_deleted(self, event):
        self._run_command(event)

    def on_modified(self, event):
        self._run_command(event)

def termed(signum, frame):
    sys.exit(0)

def watch(path):
    signal.signal(signal.SIGTERM, termed)
    event_handler = MyHandler()
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
    watch("/etc")
