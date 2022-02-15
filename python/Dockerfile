FROM python

RUN apt-get update -y
RUN apt-get install -y python3-pip

WORKDIR /project

RUN pip install mysql-connector-python

COPY . /project/