ARG PYTHON_VERSION=3.11-slim-buster

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY Pipfile.lock ./Pipfile.lock
COPY Pipfile ./Pipfile

RUN set -ex && \
    pip install -U pip && \
    pip install pipenv && \
    pipenv install --deploy --system

COPY . /app/



EXPOSE 8000

ENTRYPOINT  ["./start.sh"]