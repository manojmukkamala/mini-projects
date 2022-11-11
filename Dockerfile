FROM ubuntu:focal

EXPOSE 8888 8080 8081

COPY ./requirements.txt /

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install openjdk-11-jdk
RUN apt-get install -y python3.10 && apt install -y python3-pip

RUN pip install --no-cache-dir -r /requirements.txt