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
