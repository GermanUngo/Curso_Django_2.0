#!/bin/bash

set -euxo pipefail

python manage.py migrate --noinput
gunicorn --bind :8000 --workers 2 pypro.wsgi

#docker run --rm -it -p 8000:8000 -e SECRET_KEY=secret -e ALLOWED_HOSTS=localhost, curso-django python manage.py migrate