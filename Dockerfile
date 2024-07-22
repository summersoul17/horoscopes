FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y libyaml-dev tini && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml .

RUN poetry install

COPY . .

CMD [ "python", "main.py" ]
