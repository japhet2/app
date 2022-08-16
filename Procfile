web: gunicorn cinema.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate 
web: gunicorn cinema.wsgi
release: python manage.py makemigartions --no-input
