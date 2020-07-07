FROM python:2.7-slim

RUN apt-get update && apt-get install -y \
  xinetd \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /ctf
WORKDIR /ctf
RUN useradd -M -d /ctf ctf

RUN echo "Connection blocked" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY ./src /ctf/

RUN chown -R root:ctf /ctf && \
  chmod -R 750 /ctf && \
  chmod 740 /ctf/flag.txt

ENTRYPOINT []
CMD ["/usr/sbin/xinetd", "-dontfork"]

EXPOSE 9999
