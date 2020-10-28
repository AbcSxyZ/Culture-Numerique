FROM debian:10

COPY ./requirements.txt /requirements.txt

RUN apt update
RUN apt install -y vim

RUN apt install -y python3 python3-pip
RUN apt install -y apache2 apache2-dev libapache2-mod-wsgi-py3
RUN apt install -y certbot python-certbot-apache openssl
RUN apt install -y libz-dev libjpeg-dev libfreetype6-dev python-dev
RUN apt install -y default-libmysqlclient-dev mariadb-client
RUN apt install -y goaccess


RUN pip3 install -r /requirements.txt

COPY ./entrypoint.sh /entrypoint.sh

#RUN useradd -ms /bin/bash user_apache
# USER user_apache

WORKDIR /var/site

ENTRYPOINT bash /entrypoint.sh
