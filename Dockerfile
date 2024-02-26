FROM python:3.12.2-alpine3.17

WORKDIR /app

COPY requirements.txt app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . ./app

CMD [ "python3", "app.py"]

EXPOSE 8002