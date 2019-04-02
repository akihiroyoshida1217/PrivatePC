FROM vscode-image:latest

#RUN apt-get update -qq && \
#    apt-get install -yq --no-install-recommends curl apt-transport-https gpg && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*

#RUN mkdir -p /etc/ssl/certs && \
#    curl -k https://curl.haxx.se/ca/cacert.pem -o /etc/ssl/certs/ca-certificates.crt

#RUN curl -L https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | apt-key add - && \
#    echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends code libxtst6 libasound2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Replace 1000 with your user / group id
RUN mkdir -p /home/1000 && \
    mkdir -p /home/1000/.vscode/extensions && \
    mkdir -p /home/1001 && \
    mkdir -p /home/1001/.vscode/extensions && \
    mkdir -p /home/1002 && \
    mkdir -p /home/1002/.vscode/extensions && \
    echo "1000:x:1000:1000:1000,,,:/home/1000:/bin/bash" >> /etc/passwd && \
    echo "1001:x:1001:1001:1001,,,:/home/1001:/bin/bash" >> /etc/passwd && \
    echo "1002:x:1002:1002:1002,,,:/home/1002:/bin/bash" >> /etc/passwd && \
    echo "1000:x:1000:" >> /etc/group && \
    echo "1001:x:1001:" >> /etc/group && \
    echo "1002:x:1002:" >> /etc/group && \
    chown 1000:1000 -R /home/1000 && \
    chown 1001:1001 -R /home/1001 && \
    chown 1002:1002 -R /home/1002

USER 1002

#ENTRYPOINT ["bin/sh", "-c", "apt-get update && apt-get install -dy code"]
ENTRYPOINT ["bin/sh", "-c", "/usr/bin/code --install-extension $CODE_EXTENSION --force"]
