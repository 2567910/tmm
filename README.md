how to get on server from lars:

1. ssh lukas@173.212.252.76


Um Lars das Docker Image zu geben:

1. make docker

2. make push

3. docker login registry.woeye.net

#blu wagtail



## Installation

1. clone this project


2. install venv folder

```scala
python3 -m venv venv
```

3. Activate venv form root

```scala
source venv/bin/activate
```

4 Install reqierements
```scala
pip install -r requirements.txt
```

5. Watch file changes via npm

```scala
cd frontend
npm run watch
```

6. run server

```scala
./manage.py runserver
```

## setup postgresql

1. cd {{root (where docker-compose.yml is. Make sure the other databases are off)}}
2. rm -rf ./pgdata (if you want to remove all data)

2. docker-compose up postgres

3. run ./manage.py createsuperuser --username django

4. run ./manage.py runserver

las. docker-compose -f docker-compose-local.yml down
### Updating changes in models.py

```scala
./manage.py makemigrations
./manage.py migrate
```

### git pull

just for noobs if you have uncommited code do that:

```scala
git stash
```
now you can pull savely

```scala
git pull
```
reapply stash

```scala
git stash apply
```
### git commit

```scala
git commit -a -m "Commit text here"
git push
```
or for just commiting a single file or all files you added
```scala
git add filename folder/filename.css
git commit -m "Commit text"
```

# Dump Fixtures

User:

    $ ./manage.py dumpdata --indent 2 --natural-foreign --natural-primary auth.User > blu_beyond/fixtures/user.json

Jobs:

    $ ./manage.py dumpdata --indent 2 --natural-foreign --natural-primary jobs > blu_beyond/fixtures/jobs.json

Wagtail, grundlegendes Setup mit Homepage:

    $ ./manage.py dumpdata --indent 2 --natural-foreign --natural-primary wagtailcore > blu_beyond/fixtures/wagtail.json


### Translate (with gettext)

```scala
./manage.py makemassages

./manage.py compilemassages
git push
```
or for just commiting a single file or all files you added
```scala
git add filename folder/filename.css
git commit -m "Commit text"
```

### Whene this Error comes: (comes when deleting a migration)
Error:
```scala django.db.utils.ProgrammingError: column "language_key" of relation "menus_menu" does not exist LINE .```

# Fix:
1. Revert migrations
```scala ./manage.py migrate footers zero```

1. Reapply migrations so that de database is updated
```scala ./manage.py migrate```


### Deplyment with k8s

1. commit everything to use the right tag.

2.
```scala
make docker
```
3.
```scala
make push
```
4. Change tag in /deploy/deployment.yaml line 18 to tag from image (See Make docker)

5.
```scala
make deploy
```

6. check if everything is running ```kubectl -n lukas get pods```

7. check log files: ```kubectl -n lukas logs -f revincus-66df54d6f5-2cxpc -c django```

8. To run commands do with ./manage.py: ```kubectl exec --stdin --tty revincus-7994dfb95d-lfkl5 -c django -- /bin/bash ```
