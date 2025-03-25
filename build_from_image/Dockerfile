FROM python:3.7.6-buster
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN apt-get install -y tzdata bash curl gcc g++
RUN pip install --upgrade pip
RUN pip install psycopg2-binary beautifulsoup4 yfinance
# RUN pip install apscheduler
ADD ./requirements.txt /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt