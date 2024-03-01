FROM python:3.12.2-bookworm

WORKDIR /code

COPY ./requirements.txt ./

RUN apt install git \
    && pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app ./app

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]