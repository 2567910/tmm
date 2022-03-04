#!/bin/bash

if [ "$1" = 'runserver' ]; then

  ./manage.py migrate
  ./manage.py collectstatic

  gunicorn -b 0.0.0.0:8000 \
      --limit-request-line 0 \
      --workers 1 \
      --timeout 60 \
      --access-logfile - \
      --error-logfile - \
      tmm.wsgi
fi

exec "$@"
