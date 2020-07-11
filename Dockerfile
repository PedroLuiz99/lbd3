FROM python:3.6

RUN apt-get -y update
RUN apt-get -y upgrade 

RUN apt-get -y install python-dev libmariadb-dev

EXPOSE 5000

WORKDIR /app

RUN pip3 install setuptools==45
RUN pip3 install mysqlclient

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app
RUN python manage.py db init
CMD python manage.py run
