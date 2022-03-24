# Translation Managmant Microservice
This project provides a Django application that lets you manage translations and deliver them via REST API to any application that supports the i18next JSON format. This project is intended to be a Free open source and Self-hosted Docker alternative to existing SaaS Solutions (e.g. locize.com).
test

1. [ Setup development environment](#setup-development-environment)
3. [Usage](#usage)
4. [License](#license)
<!-- - [Dump Fixtures](#dump-fixtures) -->

<br />

## Setup development environment
### Setup Django application (local)

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/2567910/tmm.git
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

Switch back to the terminal window where the virtual env and migrate
```sh
(env)$ python manage.py migrate
```

Create a superuser
```sh
(env)$ ./manage.py createsuperuser --username YOUR_SUPERUSER_NAME
```



All done! After you run the command below the Django application should be visable under: `http://127.0.0.1:8000/admin/`.
```sh
(env)$ python manage.py runserver
```

You should be able to use the created superuser credentials to log in to the admin.

> **Disclaimer**: This project includes an example dockerfile for Production. But you should configure it to your own needs.
>
<br />



## Usage

Once you have a Django application running, and you are logged in, you should see the screen Below.

<img src="https://old.lukasseyfarth.com/kunden/blu-beyond/Bildschirmfoto%202022-03-04%20um%2015.44.42.png" width="1000"></img>

If you are logged in as an admin you should be able to create, delete and update Projects, Languages, TranslationKey and Translations.

You also have the option to Import existing .json i18next formatted translation files. Upon import, all data is overwritten, so be aware. Imported files do not have the rights to delete Translations or TranslationKeys.

<img src="https://old.lukasseyfarth.com/kunden/blu-beyond/Bildschirmfoto 2022-03-04 um 15.43.37.png" width="1000"></img>

To access the translations you have created from the REST API use the following pattern: `http://127.0.0.1:8000/translations/{PROJECT_NAME}/{LANGUAGE_CODE}`

<img src="https://old.lukasseyfarth.com/kunden/blu-beyond/Bildschirmfoto 2022-03-04 um 15.57.44.png" width="1000"></img>

We have also created a [demo React integration](https://github.com/2567910/tmm_react_integration). Feel free to use the integration code from there.
<!-- User:

    $ ./manage.py dumpdata --indent 2 --natural-foreign --natural-primary auth.User > blu_beyond/fixtures/user.json

Jobs:

    $ ./manage.py dumpdata --indent 2 --natural-foreign --natural-primary translation_management_tool > tmm/apps/translation_management_tool/fixtures/project.json

Wagtail, grundlegendes Setup mit Homepage:

    $ ./manage.py dumpdata --indent 2 --natural-foreign --natural-primary wagtailcore > blu_beyond/fixtures/wagtail.json


![Insert Header Number Sections](https://old.lukasseyfarth.com/kunden/revincus/Bildschirmfoto%202021-11-11%20um%2020.32.54.png) -->

## License
The package is Open Source Software released under the [MIT License](LICENSE). It's developed by Lukas Seyfarth.
