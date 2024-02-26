FROM python:3.12.2-alpine3.19

WORKDIR /app

COPY . .

RUN apk add git

RUN pip3 install -r requirements.txt

EXPOSE 4000

CMD [ "python3", "app/main.py"]