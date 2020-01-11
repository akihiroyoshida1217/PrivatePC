ARG imagever="latest"
FROM docker-image:${imagever}

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends docker-ce docker-ce-cli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /image

#ENTRYPOINT ["bin/sh", "-c", "apt-get update && apt-get install -dy docker-ce"]
ENTRYPOINT ["bin/sh", "-c", "docker pull debian:$pullver && docker save debian > /image/debian.tar"]
