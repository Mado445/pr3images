FROM python:3.10-slim

RUN pip install --no-cache-dir requests Flask

WORKDIR /echo

COPY echo.py .

CMD ["python3","echo.py"]

