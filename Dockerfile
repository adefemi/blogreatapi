FROM python:3.6

RUN mkdir /blogreat

WORKDIR /blogreat

COPY . /blogreat/

RUN pip install -r requirements.txt
