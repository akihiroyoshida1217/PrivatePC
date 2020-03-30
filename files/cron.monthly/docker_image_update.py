#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import docker
import traceback
import re
import subprocess

def baseimageupdate(imagename = "debian", tag = "latest"):
    subprocess.call(["imagename=" + imagename, "pullver=" + tag, "/usr/local/bin/docker-compose", 
                        "-f", "/opt/docker-image/docker-image-package/docker-compose.yml", 
                        "run", "--rm", "docker-image"])
    subprocess.call(["/usr/bin/docker", "load", "/opt/docker-image/docker-image-package/docker-image/image/" + imagename + ".tar"])

def imageupdate():
    try:
        with open("/etc/os-release") as ld:
            lines = ld.readlines()

        version_code = [line.strip() for line in lines if re.search("VERSION_CODENAME",line)][0].split("=")[1]
        
        baseimageupdate()
        baseimageupdate("debian", version_code)
        client = docker.from_env()
        #client.images.pull("debian:" + version_code)
        #client.images.pull("debian:latest")
        imagelists_with_buildarg = { "vscode-image" : "/opt/docker-image/vscode-package/vscode/" , 
                  "docker-image" : "/opt/docker-image/docker-package/docker/" , 
                  "python-image" : "/opt/docker-image/python-package/python/"}
        [ client.images.build(path = v , 
                               tag = k + ":" +  "{0:%Y%m}".format(datetime.datetime.now()), 
                               nocache = True , 
                               buildargs = { "imagever": version_code } ,
                               dockerfile = v + "Dockerfile"
                               )[0].tag(repository = k , tag = "latest") for k, v in imagelists.items() ]
        imagelists = { "firefox-image" : "/opt/docker-image/firefox-package/firefox/" , 
                  "freshclam" : "/opt/docker-image/clamav-package/clamav/" , 
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
