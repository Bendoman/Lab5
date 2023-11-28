FROM python:3.10

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app

ENV PORT 8080

WORKDIR $APP_HOME

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt
