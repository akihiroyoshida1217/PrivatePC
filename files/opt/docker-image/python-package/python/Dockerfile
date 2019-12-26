ARG imagever="latest"
FROM debian:${imagever}

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends python3 python3-pip build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir src

RUN pip3 install --no-cache-dir setuptools

ENTRYPOINT ["bin/sh", "-c", "/usr/bin/pip3 download -d src ansible docker-compose docker watchdog pylint systemd"]
