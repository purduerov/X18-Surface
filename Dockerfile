FROM ros:humble

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update
RUN apt-get -y install xorg python3-pip libxkbcommon-x11-0 libxcb* 

ADD . /X16-Surface/
WORKDIR /X16-Surface/

RUN pip3 install -r requirements.txt

RUN bash /X16-Surface/build.sh
CMD bash /X16-Surface/run.sh
