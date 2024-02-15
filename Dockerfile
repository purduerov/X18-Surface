FROM ros:humble

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update
RUN apt-get -y install xorg python3-pip ssh libxkbcommon-x11-0 libxcb* 

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /X16-Surface/
WORKDIR /X16-Surface/
RUN bash /X16-Surface/build.sh
CMD bash /X16-Surface/run.sh
