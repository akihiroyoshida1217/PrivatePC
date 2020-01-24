#!/bin/bash
 
DATESTR=`date`
sudo -u#1000 DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus /usr/bin/notify-send "$DATESTR Virus Found $CLAM_VIRUSEVENT_VIRUSNAME" 
