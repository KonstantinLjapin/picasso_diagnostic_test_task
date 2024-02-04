#!/bin/bash
# need chmod +
sleep 10s
cd app/pdtt/
python manage.py makemigrations appupload;
python manage.py migrate;
python manage.py createsuperuser --noinput;
python manage.py runserver 0.0.0.0:8000 &
celery -A pdtt worker -l INFO