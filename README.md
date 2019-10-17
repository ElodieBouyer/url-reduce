# url-reduce
Minify urls

## Prerequisites

* python3 installed
* python3-venv installed

## Project requirements

1. `python3 -m venv venv` for creating a virtual environments
2. `./venv/bin/pip install -r requirements.pip` to install project externs libs in venv

## Usage - local

1. Start the django server: `./venv/bin/python src/manage.py runserver`
2. Main URL: http://127.0.0.1:8000/

## Migrations

> This project use Django migration, see https://docs.djangoproject.com/fr/2.2/topics/migrations/

`$ ./venv/bin/python src/manage.py makemigrations reduce`

`$ ./venv/bin/python src/manage.py migrate --run-syncdb`


