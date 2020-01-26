ARG imagever="latest"
FROM debian:${imagever}

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends curl apt-transport-https gpg sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /etc/ssl/certs && \
    curl -k https://curl.haxx.se/ca/cacert.pem -o /etc/ssl/certs/ca-certificates.crt

RUN curl -L --cacert /etc/ssl/certs/ca-certificates.crt https://download.docker.com/linux/debian/gpg | gpg --dearmor > /etc/apt/trusted.gpg.d/docker.gpg && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian ${imagever} stable" > /etc/apt/sources.list.d/docker.list

RUN export uid=1011 gid=1011 && \
    mkdir -p /home/dockeruser && \
    echo "dockeruser:x:${uid}:${gid}:dockeruser,,,:/home/dockeruser:/bin/bash" >> /etc/passwd && \
    echo "dockeruser:x:${uid}:" >> /etc/group && \
    chown ${uid}:${gid} -R /home/dockeruser && \
    echo "dockeruser ALL=(ALL) NOPASSWD: /usr/bin/apt-get" >> /etc/sudoers

USER dockeruser
ENTRYPOINT ["bin/sh", "-c", "sudo apt-get update && sudo apt-get install -dy docker-ce"]
