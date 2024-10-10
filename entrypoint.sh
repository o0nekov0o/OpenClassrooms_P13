#!/bin/bash

set -e
source venv/bin/activate
if [$1 == 'gunicorn']; then
  exec gunicorn django_invoice.wsgi:application -b 127.0.0.1:8000
else
  exec python manage.py runserver 127.0.0.1:8000