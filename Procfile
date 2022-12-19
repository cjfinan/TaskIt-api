release: python manage.py makemigrations && python manage.py migrate
web: gunicorn taskit_api.wsgi