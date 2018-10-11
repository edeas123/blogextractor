
# use an official python runtime as a base image
FROM python:3.6.6

# set the working directory to /project
WORKDIR /project

# set environment variables
ENV PYTHONPATH /project

# copy the current directory content into the container at /project
COPY . /project

# install required dependencies
RUN pip install -r requirements.txt

# runtime configuration
EXPOSE 5000

# run
CMD ["uwsgi", "--ini", "uwsgi.ini"]
