FROM debian:latest

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends python3 python3-pip build-essential libssl-dev libffi-dev python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir src

RUN pip3 install --no-cache-dir setuptools

#RUN mkdir -p /etc/ssl/certs && \
#    curl -k https://curl.haxx.se/ca/cacert.pem -o /etc/ssl/certs/ca-certificates.crt
#
#RUN curl -L --cacert /etc/ssl/certs/ca-certificates.crt https://download.docker.com/linux/debian/gpg | gpg --dearmor > /etc/apt/trusted.gpg.d/docker.gpg && \
#    echo "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable" > /etc/apt/sources.list.d/docker.list


ENTRYPOINT ["bin/sh", "-c", "/usr/bin/pip3 download -d src --no-binary :all: ansible docker-compose docker watchdog pylint systemd pytest-runner setuptools_scm"]
