ARG imagever="latest"
FROM debian:${imagever}

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends curl apt-transport-https gpg sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /etc/ssl/certs && \
    curl -k https://curl.haxx.se/ca/cacert.pem -o /etc/ssl/certs/ca-certificates.crt

RUN curl -L --cacert /etc/ssl/certs/ca-certificates.crt https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list

RUN export uid=1013 gid=1013 && \
    mkdir -p /home/vscodeuser && \
    echo "vscodeuser:x:${uid}:${gid}:vscodeuser,,,:/home/vscodeuser:/bin/bash" >> /etc/passwd && \
    echo "vscodeuser:x:${uid}:" >> /etc/group && \
    chown ${uid}:${gid} -R /home/vscodeuser && \
    echo "vscodeuser:test" | chpasswd && \
    #echo "vscodeuser ALL=(ALL) NOPASSWD: /usr/bin/apt-get" >> /etc/sudoers
    echo "vscodeuser ALL=(ALL) NOPASSWD: /script/vscode-update.sh" >> /etc/sudoers

RUN mkdir /script && \
    echo "#!/usr/bin/env bash\n/usr/bin/apt-get update\n/usr/bin/apt-get install -dy code" > /script/vscode-update.sh && \
    chmod 755 /script/vscode-update.sh

USER vscodeuser
ENTRYPOINT ["sudo", "/script/vscode-update.sh"]
