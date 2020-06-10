FROM python:3

WORKDIR /crud_app

ADD ./BackEnd/requirements.txt /crud_app/requirements.txt

RUN pip install -r requirements.txt

ADD . /crud_app


