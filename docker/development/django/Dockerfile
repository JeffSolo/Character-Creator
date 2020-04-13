FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
COPY ./docker/development/django/ /build/

RUN pip install -r /build/requirements.txt

RUN mkdir /app/
WORKDIR /app/

RUN rm -r /build/
