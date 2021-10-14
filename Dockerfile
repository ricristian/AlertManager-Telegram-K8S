FROM python:3.6

LABEL maintainer="Cristian R <rionutc94@gmail.com>"

WORKDIR /alertmanager-webhook-telegram

COPY . ./

RUN pip install -r requirements.txt

RUN chmod +x flaskAlert.py

EXPOSE 9119

CMD [ "python", "./flaskAlert.py" ]
