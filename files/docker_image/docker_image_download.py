#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

params = (
    ('service', 'registry.docker.io'),
    ('scope', 'repository:library/debian:pull'),
)

token_response = requests.get('https://auth.docker.io/token', params=params)
token = json.dumps(token_response.json()['token']).strip("\"")

#print(token)

headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/vnd.docker.distribution.manifest.v2+json'
}

manifest_response = requests.get('https://registry-1.docker.io/v2/library/debian/manifests/latest', headers=headers)
#print(json.dumps(manifest_response.json()['layers'][0]['digest']))

digest = json.dumps(manifest_response.json()['layers'][0]['digest']).strip("\"")

blob_response = requests.get('https://registry-1.docker.io/v2/library/debian/blobs/' + digest , headers=headers)
#with open('/home/akihiro/PrivatePC/files/docker_image/layer.tar', 'wb') as saveFile:
#        saveFile.write(blob_response.content)

config_digest = json.dumps(manifest_response.json()['config']['digest']).strip("\"")
config_response = requests.get('https://registry-1.docker.io/v2/library/debian/blobs/' + config_digest , headers=headers)
#print(config_response.text)

blob_json = {
    "id": digest,
    "created": config_response.json().get("created"),
    "container": config_response.json().get("container"),
    "container_config": config_response.json().get("container_config"),
    "docker_version": config_response.json().get("docker_version"),
    "config": config_response.json().get("config"),
    "architecture": config_response.json().get("architecture"),
    "os": config_response.json().get("os")
  }

#print(json.dumps(blob_json))
with open('/home/akihiro/PrivatePC/files/docker_image/jsom', 'wb') as saveFile:
        json.dump(blob_json, saveFile)
