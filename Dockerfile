FROM python:3.9-alpine3.19

COPY fitness_app/requirements.txt /temp/requirements.txt
COPY fitness_app /fitness_app
WORKDIR /fitness_app
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password fitness-user

RUN apk add --no-cache redis #для redis_cli benchmark

USER fitness-user