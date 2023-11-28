### First stage
FROM python:slim

WORKDIR /home/flask-book-api

COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

EXPOSE 8080
ENTRYPOINT [ "./boot.sh" ]