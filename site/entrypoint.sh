#!/bin/bash

function create_certif()
{
    #Disable website config
    a2dissite culture-numerique
    a2ensite certbot
    service apache2 reload

    #Get ssl certificate
    certbot  certonly --staging --non-interactive --apache -d "$DOMAIN" -m "$ADMIN_MAIL" --agree-tos

    #Enable website config
    a2dissite certbot
    a2ensite culture-numerique
    service apache2 stop
}

if [ $PRODUCTION = false ]
then
    python3 manage.py runserver 0.0.0.0:$SERVER_PORT
elif [ $PRODUCTION = true ]
then
    ./manage.py collectstatic --no-input

    [ -d "/etc/letsencrypt/live/$DOMAIN" ] ||  create_certif

    apachectl -D FOREGROUND
fi

