FROM python:3.9

RUN mkdir /blogreat

WORKDIR /blogreat

COPY . /blogreat/

RUN pip install -r requirements.txt
