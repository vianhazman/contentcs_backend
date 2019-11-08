#!/bin/sh
echo "Migrating DBs."
python manage.py makemigrations
python manage.py migrate

echo "running collectstatic."
python manage.py collectstatic --noinput

#echo "Starting Gunicorn."
#exec gunicorn contentcs_service.wsgi \
#    --bind 0.0.0.0:8000

python manage.py runserver 0.0.0.0:8000
