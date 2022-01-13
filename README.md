# Translation Managmant Microservice
This project provides a Django application that lets you manage translations and deliver them via REST API to any application that supports the i18next JSON format. This project is intended to be a Free open source and Self-hosted Docker alternative to existing SaaS Solutions (e.g. locize.com).


- [Setup development environment](#setup-development-environment)
- [Setup production environment](#setup-production-environment)
<!-- - [Dump Fixtures](#dump-fixtures) -->
- [Usage](#usage)
- [License](#license)


<br /><br />

## Setup development environment
### Setup Django application (local)

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/blubeyond/tmm.git
$ cd tmm
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
Next you will need to setup the database.

<br />

### Setup Database (local)

Open another terminal window and go to the root directory of the project and run:
```sh
$ docker-compose up postgres
```

Switch back to the terminal window where the virtual env is running and create a superuser.
```sh
(env)$ ./manage.py createsuperuser --username YOUR_SUPERUSER_NAME
```

Once the user is created migrate all the changes to the database
```sh
(env)$ python manage.py migrate
```

All done! After you run the command below the Django application should be visable under: `http://127.0.0.1:8000/admin/`.
```sh
(env)$ python manage.py runserver
```

You should be able use the created superuser credentials to log in to the admin.

<br /><br />

## Setup production environment

### Setup Django application (Docker)

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/blubeyond/tmm.git
$ cd tmm
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
Next you will need to setup the database.

<br />

### Setup Database (Docker)

Open another terminal window and go to the root directory of the project and run:
```sh
$ docker-compose up postgres
```

Switch back to the terminal window where the virtual env is running and create a superuser.
```sh
(env)$ ./manage.py createsuperuser --username YOUR_SUPERUSER_NAME
```

Once the user is created migrate all the changes to the database
```sh
(env)$ python manage.py migrate
```

All done! After you run the command below the Django application should be visable under: `http://127.0.0.1:8000/admin/`.
```sh
(env)$ python manage.py runserver
```

You should be able use the created superuser credentials to log in to the admin.

<br /><br />

<!-- # Dump Fixtures

User:

    $ ./manage.py dumpdata --indent 2 --natural-foreign --natural-primary auth.User > blu_beyond/fixtures/user.json

Jobs:

    $ ./manage.py dumpdata --indent 2 --natural-foreign --natural-primary translation_management_tool > tmm/apps/translation_management_tool/fixtures/project.json

Wagtail, grundlegendes Setup mit Homepage:

    $ ./manage.py dumpdata --indent 2 --natural-foreign --natural-primary wagtailcore > blu_beyond/fixtures/wagtail.json

<br /><br /> -->

## Usage

User:

    $ ./manage.py dumpdata --indent 2 --natural-foreign --natural-primary auth.User > blu_beyond/fixtures/user.json

Jobs:

    $ ./manage.py dumpdata --indent 2 --natural-foreign --natural-primary translation_management_tool > tmm/apps/translation_management_tool/fixtures/project.json

Wagtail, grundlegendes Setup mit Homepage:

    $ ./manage.py dumpdata --indent 2 --natural-foreign --natural-primary wagtailcore > blu_beyond/fixtures/wagtail.json


![Insert Header Number Sections](https://old.lukasseyfarth.com/kunden/revincus/Bildschirmfoto%202021-11-11%20um%2020.32.54.png)

## 8. License
The package is Open Source Software released under the [MIT License](LICENSE). It's developed by blu BEYOND GmbH.