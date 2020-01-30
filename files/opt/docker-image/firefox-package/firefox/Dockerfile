FROM debian:latest

RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends firefox-esr-l10n-ja task-japanese locales locales-all ibus-mozc im-config fonts-ipafont libcanberra-gtk3-module xdg-user-dirs pulseaudio && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/1000 /home/1000/Downloads /home/1000/profile /home/1000/.local/share/gnome-shell/extensions && \
    mkdir -p /home/1001 /home/1001/Downloads /home/1001/profile /home/1001/.local/share/gnome-shell/extensions && \
    mkdir -p /home/1002 /home/1002/Downloads /home/1002/profile /home/1002/.local/share/gnome-shell/extensions && \
    echo "1000:x:1000:1000:1000,,,:/home/1000:/bin/bash" >> /etc/passwd && \
    echo "1001:x:1001:1001:1001,,,:/home/1001:/bin/bash" >> /etc/passwd && \
    echo "1002:x:1002:1002:1002,,,:/home/1002:/bin/bash" >> /etc/passwd && \
    echo "1000:x:1000:" >> /etc/group && \
    echo "1001:x:1001:" >> /etc/group && \
    echo "1002:x:1002:" >> /etc/group && \
    chown 1000:1000 -R /home/1000 && \
    chown 1001:1001 -R /home/1001 && \
    chown 1002:1002 -R /home/1002

RUN sed -e "s/# ja_JP.UTF-8/ja_JP.UTF-8/g" /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=ja_JP.utf8 && \
    im-config -n ibus

RUN mkdir /script && \
    echo "#!/usr/bin/env bash\n/usr/bin/ibus-daemon -dx\n/usr/bin/firefox -no-remote -profile /home/\$UID/profile" > /script/firefox-run.sh && \
    chmod 755 /script/firefox-run.sh

USER 1002
ENV LANG=ja_JP.utf8
ENV LANGUAGE="ja_JP:ja"
ENV XMODIFIERS="@im=ibus"
ENV GTK_IM_MODULE="xim"
ENV QT_IM_MODULE="ibus"
ENV PULSE_SERVER=unix:/tmp/pulse/native
ENV PULSE_COOKIE=/tmp/pulse/cookie
ENTRYPOINT ["/script/firefox-run.sh"]
