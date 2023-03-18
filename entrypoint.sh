#!/bin/zsh

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

celery -A store_stepik worker -l INFO &

gunicorn store_stepik.wsgi:application --bind 0.0.0.0:8000