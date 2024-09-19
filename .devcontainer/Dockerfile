# Specify base image
FROM ros:humble
ARG DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get -y update
RUN apt-get -y install python3-pip

# Install python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
