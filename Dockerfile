FROM python:3.4.2

COPY . /facehub

ADD requirements.txt /facehub/requirements.txt

RUN pip3 install -r /facehub/requirements.txt

EXPOSE 8080

CMD cd facehub && python3 facehub/app.py
