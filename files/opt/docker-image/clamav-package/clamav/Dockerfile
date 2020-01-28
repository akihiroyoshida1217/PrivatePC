FROM debian:latest

RUN export uid=1010 gid=1010 && \
    mkdir -p /home/clamav && \
    echo "clamav:x:${uid}:${gid}:clamav,,,:/home/clamav:/bin/bash" >> /etc/passwd && \
    echo "clamav:x:${gid}:" >> /etc/group && \
    chown ${uid}:${gid} -R /home/clamav

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends clamav && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER clamav
ENTRYPOINT [ "/usr/bin/freshclam" ]
