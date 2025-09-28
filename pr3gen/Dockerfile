FROM python:3.10-slim

RUN pip install --no-cache-dir requests

COPY gen.py .

WORKDIR /generate

CMD ["python3","gen.py"]