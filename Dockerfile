FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /zeon

# install dependencies

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

FROM library/postgres

COPY . /zeon

COPY init.sql /docker-entrypoint-initdb.d/
