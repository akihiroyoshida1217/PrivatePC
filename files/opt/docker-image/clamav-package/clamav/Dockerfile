ARG clamav_uid
ARG clamav_gid
FROM debian:latest

RUN mkdir -p /home/clamav && \
    echo "clamav:x:${clamav_uid}:${clamav_gid}:clamav,,,:/home/clamav:/bin/bash" >> /etc/passwd && \
    echo "clamav:x:${clamav_gid}:" >> /etc/group && \
    chown ${clamav_uid}:${clamav_gid} -R /home/clamav

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends clamav && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER clamav
ENTRYPOINT [ "/usr/bin/freshclam" ]
