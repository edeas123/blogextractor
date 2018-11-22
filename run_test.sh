#!/bin/bash
set -exo pipefail

# build docker image
docker build -t blogextractor:latest -f TestDockerfile .

# run docker image
docker run --name blogextractor_test -p 5000:5000 blogextractor:latest

# stop and remove docker container
docker container rm -f blogextractor_test
