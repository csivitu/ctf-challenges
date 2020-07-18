FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    xinetd \
    cowsay \
    && rm -rf /var/lib/apt/lists/* \
    && cp /usr/games/cowsay /bin/

RUN mkdir /ctf
WORKDIR /ctf
RUN useradd -M -d /ctf ctf

RUN chmod 600 /usr/bin/env

RUN echo "Connection blocked" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY ./src /ctf/

RUN chown -R root:ctf /ctf && \
    chmod -R 750 /ctf && \
    chmod 740 /ctf/flag.txt

ENTRYPOINT []
CMD ["/usr/sbin/xinetd", "-dontfork"]

EXPOSE 9999
