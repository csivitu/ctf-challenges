FROM alpine:latest
RUN apk add --no-cache openssh busybox-extras rsync git
RUN ssh-keygen -A
RUN ssh-keygen -N "" -f ~/.ssh/id_rsa
RUN adduser --disabled-password --gecos "" ctf
RUN mkdir chroot
RUN rsync -aqz --exclude /chroot / /chroot 2>/dev/null || :
RUN git clone https://github.com/ytdl-node/ytdl.git /chroot/home/ctf/ytdl
RUN chown root:root -R /chroot/home/ctf
RUN cp /chroot/root/.ssh/id_rsa.pub /chroot/root/.ssh/authorized_keys
RUN chmod -R 555 /chroot
RUN chmod 666 /chroot/dev/null
COPY flag.txt flag.txt
COPY script.sh script.sh
RUN chmod +x script.sh
RUN echo 'command="cat /flag.txt"' $(cat ~/.ssh/id_rsa.pub) > ~/.ssh/authorized_keys
RUN echo "root:$(($RANDOM))" | chpasswd
ENTRYPOINT []
CMD ["/bin/ash", "-c", "/usr/sbin/sshd -D & nc -lkp 9999 -e /script.sh"]
EXPOSE 9999
