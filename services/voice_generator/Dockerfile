FROM python:3.12.2-alpine3.19

WORKDIR /code

COPY ./requirements.txt .

RUN apk add git \
    && apk add ffmpeg \
    && pip3 install -r /code/requirements.txt

COPY ./app ./app

EXPOSE 8080

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]