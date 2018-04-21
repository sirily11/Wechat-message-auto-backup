FROM python:3

WORKDIR /usr/src/app/wechat
RUN pip install pyrebase
RUN pip install itchat

CMD [ "python","itchat.py"]
