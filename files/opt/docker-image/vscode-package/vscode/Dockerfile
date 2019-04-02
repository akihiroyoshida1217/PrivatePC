FROM debian:latest

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends curl apt-transport-https gpg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /etc/ssl/certs && \
    curl -k https://curl.haxx.se/ca/cacert.pem -o /etc/ssl/certs/ca-certificates.crt

RUN curl -L https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | apt-key add - && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list

ENTRYPOINT ["bin/sh", "-c", "apt-get update && apt-get install -dy code"]
