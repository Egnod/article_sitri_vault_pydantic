FROM python:3.8.3-buster

ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1


RUN pip install poetry

RUN mkdir /superapp/
WORKDIR /superapp/

COPY ./pyproject.toml ./poetry.lock /superapp/
RUN poetry install --no-ansi

WORKDIR /
