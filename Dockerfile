# Django
FROM python:3.9.10-alpine
LABEL maintainer="lars.hoss@posteo.de"
ENV PYTHONUNBUFFERED=1 \
    LANG=de_DE.UTF-8 \
    DJANGO_SETTINGS_MODULE=tmm.settings.production \
    APP_BASE_DIR="/app"

RUN apk add --no-cache abuild build-base bash postgresql-dev \
    && cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime \
    && echo "Europe/Berlin" > /etc/timezone

WORKDIR $APP_BASE_DIR

COPY requirements.txt $APP_BASE_DIR/
RUN pip3 install -U pip setuptools gunicorn \
    && pip3 install -r requirements.txt \
    && rm -rf /root/.cache

COPY manage.py docker-entrypoint.sh $APP_BASE_DIR/
COPY tmm $APP_BASE_DIR/tmm

EXPOSE 8000
ENTRYPOINT [ "./docker-entrypoint.sh" ]
CMD ["runserver"]
