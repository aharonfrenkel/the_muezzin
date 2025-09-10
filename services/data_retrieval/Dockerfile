FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get upgrade --yes

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

CMD ["python", "main.py"]