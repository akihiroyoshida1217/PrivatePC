#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import os
import tarfile

image_name = 'debian'
tag = 'latest'

os.makedirs(image_name)

params = (
    ('service', 'registry.docker.io'),
    ('scope', 'repository:library/' + image_name + ':pull'),
)

token_response = requests.get('https://auth.docker.io/token', params=params)
token = json.dumps(token_response.json()['token']).strip("\"")

#print(token)

headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/vnd.docker.distribution.manifest.v2+json'
}

manifest_response = requests.get('https://registry-1.docker.io/v2/library/' + image_name + '/manifests/' + tag, headers=headers)
#print(json.dumps(manifest_response.json()['layers'][0]['digest']))

config_digest = json.dumps(manifest_response.json()['config']['digest']).strip("\"")
config_response = requests.get('https://registry-1.docker.io/v2/library/' + image_name + '/blobs/' + config_digest , headers=headers)
#print(config_response.text)
with open(image_name + '/' + config_digest.replace('sha256:','') + '.json', 'w') as saveCONFIG:
        saveCONFIG.write(config_response.text)

manifest_json = [{
    "config": config_digest.replace('sha256:','') + ".json",
    "RepoTags": [
      image_name + ":" + tag
    ],
    "Layers": [ d['digest'].replace('sha256:','') + '/layer.tar' for d in manifest_response.json()['layers'] ]
  }]
#print(json.dumps(manifest_json))
with open(image_name + '/' + 'manifest.json', 'w') as saveMANIFEST:
        json.dump(manifest_json, saveMANIFEST)

repositories_json = {
    image_name : {
      tag : manifest_response.json()['layers'][-1]['digest'].replace('sha256:','')
    }
  }
#print(json.dumps(repositories_json))
with open(image_name + '/' + 'repositories', 'w') as saveREPOSITORIES:
        json.dump(repositories_json, saveREPOSITORIES)

digest = json.dumps(manifest_response.json()['layers'][0]['digest']).strip("\"")

os.makedirs(image_name + '/' + digest.replace('sha256:',''))

blob_response = requests.get('https://registry-1.docker.io/v2/library/' + image_name + '/blobs/' + digest , headers=headers)
with open(image_name + '/' + digest.replace('sha256:','') + '/layer.tar', 'wb') as saveFile:
        saveFile.write(blob_response.content)

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
with open(image_name + '/' + digest.replace('sha256:','') + '/json', 'w') as saveJSON:
        json.dump(blob_json, saveJSON)

with open(image_name + '/' + digest.replace('sha256:','') + '/VERSION', 'w') as saveVERSION:
        saveVERSION.write('1.0')

with tarfile.open(image_name + '.tar', 'w') as tar:
        tar.add(image_name + '/')