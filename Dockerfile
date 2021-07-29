FROM python:3.7-slim-buster as base

WORKDIR /app

RUN apt-get update -y && \
  apt-get install --no-install-recommends -y openssl openssh-client && \
  apt-get clean all

##### Build Environment #####
FROM base as builder

RUN apt-get update -y && \
  apt-get install -y wget

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Upgrade pip3
RUN pip3 install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . .

##### Dev/Test Build #####
FROM builder as dev

##### Release Build #####
FROM base as release

COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app

