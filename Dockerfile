#pull official base image
FROM python:3.10-slim
RUN apt-get update
RUN apt-get install python3-dev build-essential -y

# set envoroment variable 
ENV PYTHONDONWRITEBYTECCODE 1
ENV VIRTUAL_ENV = /opt/venv
# pip requirements
RUN pip3 install --upgrade pip
# RUN pip3 install virtualenv && python3 -m virtualenv ${VIRTUAL_ENV}
# ENV PATH='${VIRTUAL_ENV}:${PATH}'
ADD ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
COPY . /srv/app
WORKDIR /srv/app



