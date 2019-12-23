FROM debian:latest

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends curl apt-transport-https gpg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /etc/ssl/certs && \
    curl -k https://curl.haxx.se/ca/cacert.pem -o /etc/ssl/certs/ca-certificates.crt

RUN curl -L --cacert /etc/ssl/certs/ca-certificates.crt http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0xEAC0D406E5D79A82ADEEDFDFB76E53652D87398A | gpg --dearmor > /etc/apt/trusted.gpg.d/adapta.gpg && \
    curl -L --cacert /etc/ssl/certs/ca-certificates.crt http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0xD320D0C30B02E64C5B2BB2743766223989993A70 | gpg --dearmor > /etc/apt/trusted.gpg.d/paper.gpg && \
    echo "deb http://ppa.launchpad.net/snwh/ppa/ubuntu bionic main" > /etc/apt/sources.list.d/ppa.list
    echo "deb http://ppa.launchpad.net/tista/adapta/ubuntu bionic main" > /etc/apt/sources.list.d/ppa.list

ENTRYPOINT ["bin/sh", "-c", "apt-get update && apt-get install -dy adapta-gtk-theme paper-icon-theme"]
