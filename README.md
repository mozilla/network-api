# Mozilla Network Site API

This is the REST API server for the Mozilla Network Site.

## Requirements

The only requirement to run this API is Docker and its dependencies (which you can [download here](https://www.docker.com/products/docker)). Make sure you have port 5000 open as the API is exposed on that port.

## Setup

Before you can run the site, you'll need to run the migrations and create a superuser. These commands are run within the container:

```bash
docker-compose run web sh -c "python manage.py migrate"
docker-compose run web sh -c "python manage.py createsuperuser"
```

To build and run the API, simply run:
```bash
docker-compose up
```
You should now be able to access the API on `localhost:5000`.

To log in to the admin UI, visit:
http://localhost:5000/admin

Any changes you make in the `app` directory will automatically be reflected in the docker container.

**Note:** If you change anything involved the build (for e.g. change the requirements), you will need to run `docker-compose up --build` so that it will re-build your container with the changes.

As this is a Python/Django project, we also support additional commands that might be of use. To run a command, simply run:
```bash
docker-compose run web sh -c "<command>"
```
where, `<command>` (don't forget about the surrounding quotes) should be replaced by any one of the following:

| No. | Command | Description |
| --- | ------- | ----------- |
| 1. | flake8 . | Run Flake8 linting on the code.  |
| 2. | python manage.py test | Run the tests defined for this project. |
| 3. | python manage.py makemigrations | Create migration files for all Django model changes detected. |
| 4. | python manage.py migrate | Apply migrations to the database. |
| 5. | python manage.py shell | Open up a Python interactive shell. |
| 6. | python manage.py createsuperuser | Create a super user for the Django administrative interface. |
| 7. | python manage.py collectstatic | Create a folder containing all the static content that needs to be served for use by the API and the admin interface. |

## Reset dev environment

If you ~~really mess things up~~ want to start fresh, delete your local database within docker and try again.

`docker-compose down --rmi local` and `docker-compose up`. You'll need to `migrate` and `createsuperuser` again, using the above instructions.

## Our deployment diagram

[![](screenshot.184.png)](https://www.lucidchart.com/documents/edit/72261654-23d0-491c-b67e-c026abbafcd3)
