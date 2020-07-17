FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y \
    lib32z1 \
    xinetd \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf

WORKDIR /ctf

RUN echo "Connection blocked" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY . .

RUN chmod -R 755 /ctf

ENTRYPOINT []
CMD ["/usr/sbin/xinetd", "-dontfork"]

EXPOSE 9999