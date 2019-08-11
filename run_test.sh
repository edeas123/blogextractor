#!/bin/bash
set -exo pipefail

# build, create and start containers
docker-compose -f test-docker-compose.yml up --build --abort-on-container-exit

# stop and remove containers
docker-compose -f test-docker-compose.yml down --rmi local
