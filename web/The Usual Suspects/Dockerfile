FROM python:3.7-slim
RUN pip install tornado
WORKDIR /ctf
COPY . .
RUN useradd -M ctf
RUN chown -R root:root /ctf
RUN chmod -R 700 /ctf
CMD ["python", "server.py"]
EXPOSE 9999