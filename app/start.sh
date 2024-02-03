#!/bin/bash
# need chmod +
sleep 10s
python app/pdtt/manage.py makemigrations appupload;
python app/pdtt/manage.py migrate;
python app/pdtt/manage.py createsuperuser --noinput;
python app/pdtt/manage.py runserver 0.0.0.0:8000
