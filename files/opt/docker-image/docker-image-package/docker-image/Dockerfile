ARG imagever="latest"
FROM debian:${imagever}

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir requests

RUN mkdir /image && \
    mkdir /script

COPY docker_image_download.py /script/

RUN export uid=1014 gid=1014 && \
    mkdir -p /home/imageuser && \
    echo "imageuser:x:${uid}:${gid}:imageuser,,,:/home/imageuser:/bin/bash" >> /etc/passwd && \
    echo "imageuser:x:${uid}:" >> /etc/group && \
    chown ${uid}:${gid} -R /home/imageuser && \
    echo "imageuser:test" | chpasswd && \
    chmod 755 /script/docker_image_download.py && \
    chown ${uid}:${gid} -R /image

USER imageuser
ENTRYPOINT ["/script/docker_image_download.py"]
