FROM debian:10

COPY ./requirements.txt /requirements.txt

RUN apt update
RUN apt install -y vim

RUN apt install -y python3 python3-pip

RUN pip3 install -r /requirements.txt


ENTRYPOINT python3 /var/site/manage.py runserver 0.0.0.0:8000
