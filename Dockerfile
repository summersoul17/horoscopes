FROM python:3.10 AS base

ARG POETRY_HOME=/etc/poetry
RUN apt-get update && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y libyaml-dev curl tini && \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python - --version 1.8.2 && \
    apt-get remove -y curl && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="${PATH}:${POETRY_HOME}/bin"

COPY poetry.lock pyproject.toml ./

FROM base as development

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-cache

ENV PYTHONPATH=/
COPY main.py ./main.py
COPY src ./src
COPY .env ./.env
COPY config.py ./config.py
#RUN ["python", "./main.py"]
