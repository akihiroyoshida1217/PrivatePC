ARG imagever="latest"
FROM debian:${imagever}

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends curl apt-transport-https gpg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /etc/ssl/certs && \
    curl -k https://curl.haxx.se/ca/cacert.pem -o /etc/ssl/certs/ca-certificates.crt

RUN curl -L --cacert /etc/ssl/certs/ca-certificates.crt https://download.docker.com/linux/debian/gpg | gpg --dearmor > /etc/apt/trusted.gpg.d/docker.gpg && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian ${imagever} stable" > /etc/apt/sources.list.d/docker.list

ENTRYPOINT ["bin/sh", "-c", "apt-get update && apt-get install -dy docker-ce"]
