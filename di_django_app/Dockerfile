FROM python:3

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

# COPY ./docker_settings/.env /app/
# COPY ./docker_settings/db.cnf /app/