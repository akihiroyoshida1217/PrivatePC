#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import os
import tarfile
import subprocess
import shutil
import sys

token_url = 'https://auth.docker.io/token'
request_url = 'https://registry-1.docker.io/v2/library/'

def layerdownload(image_name, headers, digest, config_response):
        layer_path = image_name + '/' + digest.replace('sha256:','')
        
        os.makedirs(layer_path)

        blob_response = requests.get(request_url + image_name + '/blobs/' + digest , headers=headers)

        blob_json = {
            "id": digest.replace('sha256:',''),
            "created": config_response.json().get("created"),
            "container": config_response.json().get("container"),
            "container_config": config_response.json().get("container_config"),
            "docker_version": config_response.json().get("docker_version"),
            "config": config_response.json().get("config"),
            "architecture": config_response.json().get("architecture"),
            "os": config_response.json().get("os")
          }
        #print(json.dumps(blob_json))

        with open(layer_path + '/layer.tar', 'wb') as saveFile, \
             open(layer_path + '/json', 'w') as saveJSON, \
             open(layer_path + '/VERSION', 'w') as saveVERSION:
                saveFile.write(blob_response.content)
                json.dump(blob_json, saveJSON)
                saveVERSION.write('1.0')

def imagedownload(image_name = 'debian', tag = 'latest'):
        try:
          os.remove(image_name + '.tar')
          shutil.rmtree(image_name)
        except FileNotFoundError:
          None
        os.makedirs(image_name)

        params = (
                ('service', 'registry.docker.io'),
                ('scope', 'repository:library/' + image_name + ':pull'),
        )

        token_response = requests.get(token_url, params=params)
        token = json.dumps(token_response.json()['token']).strip("\"")
        #print(token)

        headers = {
                'Authorization': 'Bearer ' + token,
                'Accept': 'application/vnd.docker.distribution.manifest.v2+json'
        }

        manifest_response = requests.get(request_url + image_name + '/manifests/' + tag, headers=headers)
        #print(json.dumps(manifest_response.json()['layers'][0]['digest']))

        config_digest = json.dumps(manifest_response.json()['config']['digest']).strip("\"")
        config_response = requests.get(request_url + image_name + '/blobs/' + config_digest , headers=headers)
        #print(config_response.text)

        repositories_json = {
            image_name : {
              tag : manifest_response.json()['layers'][-1]['digest'].replace('sha256:','')
            }
          }
        #print(json.dumps(repositories_json))

        manifest_json = [{
            "config": config_digest.replace('sha256:','') + ".json",
            "RepoTags": [
              image_name + ":" + tag
            ],
            "Layers": [ d['digest'].replace('sha256:','') + '/layer.tar' for d in manifest_response.json()['layers'] ]
          }]
        #print(json.dumps(manifest_json))

        with open(image_name + '/' + config_digest.replace('sha256:','') + '.json', 'w') as saveCONFIG, \
             open(image_name + '/' + 'manifest.json', 'w') as saveMANIFEST, \
             open(image_name + '/' + 'repositories', 'w') as saveREPOSITORIES:
                saveCONFIG.write(config_response.text)
                json.dump(manifest_json, saveMANIFEST)
                json.dump(repositories_json, saveREPOSITORIES)

        #digest = json.dumps(manifest_response.json()['layers'][0]['digest']).strip("\"")

        [layerdownload(image_name, headers, json.dumps(layer['digest']).strip("\""), config_response) for layer in manifest_response.json()['layers']]

        #with tarfile.open(image_name + '.tar', 'w') as tar:
        #        tar.add(image_name + '/')
        subprocess.call(["tar", "cvf", image_name + ".tar", "-C", image_name, "."])

if __name__ == "__main__":
        args = sys.argv
        if 3 == len(args):
          imagedownload(args[1], args[2])
        elif 1 == len(args):
          imagedownload()