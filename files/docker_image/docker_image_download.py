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
print(manifest_response.text)
#blob_response = requests.get('https://registry-1.docker.io/v2/library/ubuntu/blobs/$%7BBLOBSUM%7D', headers=headers)
