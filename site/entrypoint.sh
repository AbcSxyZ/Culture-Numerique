#!/bin/bash

function create_certif()
{
    #Disable website config
    a2dissite culture-numerique
    a2ensite certbot
    service apache2 reload

    #Get ssl certificate
    certbot  certonly --non-interactive --apache -d "$DOMAIN" -m "$ADMIN_MAIL" --agree-tos

    #Enable website config
    a2dissite certbot
    a2ensite culture-numerique
    service apache2 stop
}

if [ $PRODUCTION = false ]
then
    sleep 10 && ./manage.py migrate
    python3 manage.py runserver 0.0.0.0:$SERVER_PORT
elif [ $PRODUCTION = true ]
then
    #Create ssl certificate if not already available
    [ -d "/etc/letsencrypt/live/$DOMAIN" ] ||  create_certif

    #Django setup
    ./manage.py collectstatic --no-input
    sleep 5 && ./manage.py migrate

    apachectl -D FOREGROUND
fi

