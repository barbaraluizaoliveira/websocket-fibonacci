FROM python:3-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app:$PYTHONPATH

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN adduser --disabled-password --gecos "" appuser
RUN chown -R appuser /app
USER appuser

EXPOSE 8000

CMD python app/server.py
