FROM python:3

WORKDIR /usr/src/app/flask
COPY . .

RUN pip install chatterbot

CMD [ "python","chatbot.py"]

