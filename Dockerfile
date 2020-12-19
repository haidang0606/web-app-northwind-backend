# FROM ubuntu:16.04
FROM python:3.7-slim

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

# ENTRYPOINT [ "python" ]
ENV host 172.27.110.251
ENV port 5432
ENV user postgres
ENV database postgres

# CMD [ "app.py" ]
CMD [ "flask", "run", "--host", "0.0.0.0" ]