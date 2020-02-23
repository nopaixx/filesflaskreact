# FROM localhost:5000/mypython:latest
FROM python:3.7


EXPOSE 8081

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    apt-get install python-mysqldb && \ 
    apt-get install libbz2-dev


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

# RUN pip install -e .
COPY . /app
