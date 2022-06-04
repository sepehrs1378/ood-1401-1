# pull the official base image
FROM python:3.9-slim


LABEL maintainer="m.dehghankar@outlook.com"
LABEL description="Docker image for Home Service Project"

# set work directory
WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql make \
    && apt-get clean

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 8000

CMD make complete-run