FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  xinetd \
  python3-pip \
  python3-dev \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /ctf
WORKDIR /ctf
RUN useradd -M -d /ctf ctf

RUN echo "Connection blocked" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY ./src /ctf/

RUN chown -R ctf:ctf /ctf && chmod -R 770 /ctf
RUN su ctf -c "pip3 install pycryptodome==3.4.3"
RUN pip3 install pycryptodome==3.4.3

RUN chown -R root:ctf /ctf && \
  chmod -R 750 /ctf


ENTRYPOINT []
CMD ["/usr/sbin/xinetd", "-dontfork"]

EXPOSE 9999
