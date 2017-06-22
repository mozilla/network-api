# Mozilla Network Site API

This is the REST API server for the Mozilla Network Site.

## Requirements

- `python3`, `pip`, optionally `virtualenv`

## Installation

Create a virtual environment using either `virtualenv` or `python3`'s virtual enviroment invokation. For the purposes of this README.md it is assumed you called this virtual enviroment `venv`.

Activate the virtual enviroment:

- Unix/Linux/OSX: `source venv/bin/activate`
- Windows: `venv\Scripts\Activate`

(for both, the virtual enviroment can be deactivated by running the corresponding "deactivate" command)

Install all dependencies into the virtual environment:

```bash
pip install -r requirements.txt
```

## Setup

Before you can run the site, you'll need to run the migrations and create a superuser:

```bash
python app/manage.py migrate
python app/manage.py createsuperuser
```

You can now run the server using:

```
python app/manage.py runserver
```

You should now be able to access the API on `localhost:5000`.

To log in to the admin UI, visit:
http://localhost:8000/admin

As this is a Python/Django project, we also support additional commands that might be of use. Please consult the following table for some common commands you might want to use:

| No. | Command | Description |
| --- | ------- | ----------- |
| 1. | flake8 . | Run Flake8 linting on the code.  |
| 2. | python app/manage.py test | Run the tests defined for this project. |
| 3. | python app/manage.py makemigrations | Create migration files for all Django model changes detected. |
| 4. | python app/manage.py migrate | Apply migrations to the database. |
| 5. | python app/manage.py shell | Open up a Python interactive shell. |
| 6. | python app/manage.py createsuperuser | Create a super user for the Django administrative interface. |
| 7. | python app/manage.py collectstatic | Create a folder containing all the static content that needs to be served for use by the API and the admin interface. |

## Deployment considerations

If you're deploying this application behind a proxy or CDN (like CloudFront) be sure that the `X-Forwarded-Host` header is forwarded to the server, and that `USE_X_FORWARDED_HOST` is set to `True` in your server environment.

## Our deployment diagram

[![](screenshot.184.png)](https://www.lucidchart.com/documents/edit/72261654-23d0-491c-b67e-c026abbafcd3)
