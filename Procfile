release: python app/manage.py migrate
web: cd app && gunicorn networkapi.wsgi:application
