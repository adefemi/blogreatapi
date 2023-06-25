FROM python:3.8

RUN mkdir /blogreat

WORKDIR /blogreat

COPY . /blogreat/

RUN pip install -r requirements.txt
