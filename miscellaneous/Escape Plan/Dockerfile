FROM python:3.7-slim

RUN apt-get update && apt-get install -y \
  xinetd \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /ctf
WORKDIR /ctf
RUN useradd -M -d /ctf ctf

RUN chmod 1733 /tmp /var/tmp /dev/shm

RUN echo "Connection blocked" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY ./src /ctf/
RUN mv /ctf/dotgit /ctf/.git

RUN chown -R root:ctf /ctf && \
  chmod -R 750 /ctf && \
  chmod -R 740 /ctf/.git/*

ENTRYPOINT []
CMD ["/usr/sbin/xinetd", "-dontfork"]

EXPOSE 9999
