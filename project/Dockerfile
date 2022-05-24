FROM python:3.10.1-slim-buster

WORKDIR /usr/src/api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean \
  && pip3 install poetry

COPY poetry.lock . 
COPY pyproject.toml .
RUN poetry config virtualenvs.create false \
  && poetry install 

COPY . .

COPY ./entrypoint.sh .
RUN chmod 777 /usr/src/api/entrypoint.sh

ENTRYPOINT ["/usr/src/api/entrypoint.sh"]
