FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /drf_learning

COPY . /drf_learning/

RUN apt-get update

COPY ./requirements.txt .
RUN pip install -r requirements.txt