 
FROM python:3.8-slim

RUN useradd -m ctf

WORKDIR /chal

COPY . .

ENV PORT 9999
RUN pip3 install --upgrade --no-cache-dir -r requirements.txt

RUN chown -R root:ctf /chal && \
    chmod 750 /chal /chal/server.py && \
    chmod 740 /chal/flag.txt

USER ctf
CMD ["/usr/local/bin/python", "/chal/server.py"]

EXPOSE 9999