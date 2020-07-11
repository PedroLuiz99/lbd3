# Use an official Python runtime as an image
FROM python:3.6

RUN apt-get -y update
RUN apt-get -y upgrade 

RUN apt-get -y install python-dev libmariadb-dev telnet nmap

# The EXPOSE instruction indicates the ports on which a container 
# will listen for connections
# Since Flask apps listen to port 5000  by default, we expose it
EXPOSE 5000

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction 
# creates a directory with this name if it doesn’t exist
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip3 install setuptools==45
RUN pip3 install mysqlclient

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

# Run app.py when the container launches
COPY . /app
RUN rm -rf migrations
RUN python manage.py db init
CMD python manage.py run
