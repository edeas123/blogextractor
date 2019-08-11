# use project base image
FROM python:3.6.6-stretch

# set the working directory to /project
WORKDIR /project

# set environment variables
ENV PYTHONPATH /project

# copy the requirements file
COPY requirements.txt requirements.txt

# install required dependencies
RUN pip3 install -r requirements.txt

# copy the current directory content into the container at /project
COPY . .
