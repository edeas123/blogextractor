#!/usr/bin/env bash

# login to docker hub
docker login -u $DOCKER_HUB_USERNAME -p $DOCKER_HUB_PASSWORD

# build docker image
docker build -t blogextractor:latest ../.

# push docker image
docker tag blogextractor:latest edeas123/blogextractor:latest
docker push edeas123/blogextractor:latest

