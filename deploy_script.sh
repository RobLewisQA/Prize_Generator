#!/bin/bash

scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@manager-main:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@manager-main << EOF
    export DATABASE_URI=$(DATABASE_URI)
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml
EOF