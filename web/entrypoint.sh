#!/bin/bash
APP_PORT=${PORT:-8000}
cd /hobbysite/
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm hobbysite.wsgi:application --bind "0.0.0.0:${APP_PORT}"