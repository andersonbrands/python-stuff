FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY pyproject.toml .

RUN mkdir ./src \
    && pip install --no-cache-dir --upgrade pip setuptools \
    && pip install --no-cache-dir -e .[test,dev]

COPY . .

CMD ["main"]
