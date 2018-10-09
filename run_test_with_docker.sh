#!/bin/bash -e

# build docker image
docker build -t blogextractor:latest -f TestDockerfile .

# run docker image
docker run --name blogextractor -p 5000:5000 blogextractor:latest

# stop and remove docker container
docker container rm -f blogextractor
