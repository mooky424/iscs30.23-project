#!/bin/bash
APP_PORT=${PORT:-8000}
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"admin@example.com"}
cd /hobbysite/
/opt/venv/bin/python manage.py collectstatic
/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm hobbysite.wsgi:application --bind "0.0.0.0:${APP_PORT}"