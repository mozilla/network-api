FROM python:3.6

WORKDIR /app
EXPOSE 5000
COPY ./requirements.txt .
RUN pip install -r requirements.txt ipdb==0.9.3 --no-cache-dir --disable-pip-version-check
COPY ./app .
COPY ./scripts/prepare_container.sh ../
