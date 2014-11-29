FROM python:3.4.2

ADD requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD python3 app.py
