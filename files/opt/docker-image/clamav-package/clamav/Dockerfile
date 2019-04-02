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

# Replace 1000 with your user / group id
#RUN export uid=1000 gid=1000 && \
#    mkdir -p /home/developer && \
#    echo "developer:x:${uid}:${gid}:Developer,,,:home/developer:/bin/bash" >> /etc/passwd && \
#    echo "developer:x:${uid}:" >> /etc/group && \
#    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
#    chmod 0440 /etc/sudoers.d/developer && \
#    chown ${uid}:${gid} -R /home/developer

#USER developer
USER clamav
#ENV HOME /home/developer
#CMD /usr/bin/freshclam
ENTRYPOINT [ "/usr/bin/freshclam" ]
