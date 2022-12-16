FROM python:3.8-slim

# Install curl and nc
RUN apt-get update; apt-get install -y curl; apt-get install -y netcat

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /bot/

WORKDIR /bot

RUN poetry install --no-root --no-dev
RUN pip install -U --pre aiogram

COPY ./app /bot/app

ENTRYPOINT sleep 15;PYTHONPATH=/bot poetry run python ./app/run_bot.py