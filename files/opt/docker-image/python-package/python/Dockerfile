ARG imagever="latest"
FROM debian:${imagever}

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends python3 python3-pip build-essential sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir src

RUN pip3 install --no-cache-dir setuptools

RUN export uid=1012 gid=1012 && \
    mkdir -p /home/pythonuser && \
    echo "pythonuser:x:${uid}:${gid}:pythonuser,,,:/home/pythonuser:/bin/bash" >> /etc/passwd && \
    echo "pythonuser:x:${uid}:" >> /etc/group && \
    chown ${uid}:${gid} -R /home/pythonuser && \
    echo "pythonuser:test" | chpasswd && \
    echo "pythonuser ALL=(ALL) NOPASSWD:/usr/bin/pip3 download -d src ansible docker-compose docker watchdog pylint systemd dnspython" >> /etc/sudoers
    #echo "pythonuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER pythonuser
ENTRYPOINT ["sudo", "/usr/bin/pip3", "download", "-d", "src", "ansible", "docker-compose", "docker", "watchdog", "pylint", "systemd", "dnspython"]
