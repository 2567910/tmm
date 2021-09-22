# Translation Management Microservice

Todos:

Build chained backend functunality https://github.com/i18next/i18next-chained-backend



## Getting started

1. setup the postgress via `docker-compose up`
2. setup the virtualenv with:
    * Python 2:
    `virtualenv env`

    * Python 3:
    `python3 -m venv env`
3. activate the virtualenv with `source env/bin/activate`
4. install all the python dependencies with `pip install -r requirements.txt`
5. create a django superuser `./manage.py createsuperuser`
6. migrate all changes `./manage.py migrate`
7. start the development server `./manage.py runserver`

You're ready to go! your dev server is started at port :8000!
