ARG imagever="latest"
FROM debian:${imagever}

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends python3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /image

COPY docker_image_download.py /image/

RUN export uid=1014 gid=1014 && \
    mkdir -p /home/imageuser && \
    echo "imageuser:x:${uid}:${gid}:imageuser,,,:/home/imageuser:/bin/bash" >> /etc/passwd && \
    echo "imageuser:x:${uid}:" >> /etc/group && \
    chown ${uid}:${gid} -R /home/imageuser && \
    echo "imageuser:test" | chpasswd && \
    chmod 755 /image/docker_image_download.py

USER imageuser
ENTRYPOINT ["/image/docker_image_download.py", "$imagename", "$tag"]
