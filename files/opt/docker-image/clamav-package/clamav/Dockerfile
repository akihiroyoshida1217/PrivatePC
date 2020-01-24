FROM debian:latest

# Replace 1000 with your user / group id
RUN export uid=1001 gid=1001 && \
    mkdir -p /home/clamav && \
    echo "clamav:x:${uid}:${gid}:clamav,,,:/home/clamav:/bin/bash" >> /etc/passwd && \
    echo "clamav:x:${uid}:" >> /etc/group && \
    chown ${uid}:${gid} -R /home/clamav

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends clamav && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER clamav
ENTRYPOINT [ "/usr/bin/freshclam" ]
