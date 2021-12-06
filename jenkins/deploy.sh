#!/bin/bash

echo "Deploy stage"

scp docker-compose.yaml jenkins@ci-swarm-manager:/home/jenkins/docker-compose.yaml
ssh jenkins@ci-swarm-manager \
    DOCKER_HUB_CREDS_USR=$DOCKER_HUB_CREDS_USR \
    DATABASE_URI=$DATABASE_URI \
    CREATE_SCHEMA=true \
    docker stack deploy --compose-file docker-compose.yaml bc-app