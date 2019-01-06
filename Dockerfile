# use project base image
FROM edeas123/blogbase

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

# create required directories
RUN mkdir /var/log/uwsgi\
    && mkdir -p /etc/supervisor/conf.d/

# add configuration files
RUN echo_supervisord_conf >> /etc/supervisor/supervisord.conf\
    && printf "\n[include]\nfiles=conf.d/*.conf" >> /etc/supervisor/supervisord.conf\
    && cp /project/nginx.conf /etc/nginx/conf.d/nginx.conf\
    && cp /project/supervisord.conf /etc/supervisor/conf.d/blogextractor.conf


