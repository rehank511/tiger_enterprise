FROM ubuntu:latest
RUN apt-get update -y
RUN apt upgrade -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install netifaces
EXPOSE 8080
COPY /webapi2.py /
CMD ["python3", "/webapi2.py"]
