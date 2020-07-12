FROM python:3.7-slim
RUN pip install tornado
WORKDIR /ctf
COPY . .
RUN chmod -R 755 /ctf
RUN chmod -R 711 /ctf/*
RUN useradd -M ctf
USER ctf
CMD ["python", "server.py"]
