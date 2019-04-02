#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import docker
import traceback

def imageupdate():
    try:
        client = docker.from_env()
        client.images.pull("debian:latest")
        imagelists = { "firefox-image" : "/opt/docker-image/firefox-package/firefox/" , 
                  "freshclam" : "/opt/docker-image/clamav-package/clamav/" , 
                  "vscode-image" : "/opt/docker-image/vscode-package/vscode/" , 
                  "vscode-extension-image" : "/opt/docker-image/vscode-extension-package/vscode-extension/"}
        [ client.images.build(path = v , 
                               tag = k + ":" +  "{0:%Y%m}".format(datetime.datetime.now()), 
                               nocache = True , 
                               dockerfile = v + "Dockerfile"
                               )[0].tag(repository = k , tag = "latest") for k, v in imagelists.items() ]
    except:
        traceback.print_exc()

if __name__ == "__main__":
    imageupdate()