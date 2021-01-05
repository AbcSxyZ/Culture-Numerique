# Culture Numérique

Source code of [Culture Numérique](https://culture-numerique.xyz/) website.

## Installation

### Dependencies

You need to install [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) to run the website

### Launch website

Rename `.env.template` to `.env`.

Fill environment variables inside `.env`, all variables are mandatory.

Run `docker-compose up`. Your server is available at `DOMAIN` on port 80 or 443.

#### Environment variables

`DB_ROOT_PASS`, `DB_PASS`, `DB_USER`, `DB_NAME`, `DB_HOST`, `DB_PORT` : database settings.

`PRODUCTION` : Set true if server is used in production, false for developpement.
`SERVER_PORT` : port used by http server, 443 for https is open by default.
`DOMAIN` : Domain name of the website.

`ADMIN_MAIL` : Mail of the administrator of django website.

`EMAIL_USER`, `EMAIL_PASS`, `EMAIL_HOST`, `EMAIL_PORT` : e-mail settings of the address used by django server.

`SECRET_KEY` : Django's secret key.
