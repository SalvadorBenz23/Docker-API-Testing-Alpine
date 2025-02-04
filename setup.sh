#!/bin/bash

#docker image pull datascientest/fastapi:1.0.0

#docker volume create api_test

#sudo cp -v authentication_test/authentication_test.py /var/lib/docker/volumes/api_test/_data
#sudo cp -v authorization_test/authorization_test.py /var/lib/docker/volumes/api_test/_data
#sudo cp -v content_test/content_test.py /var/lib/docker/volumes/api_test/_data

# Build test images
docker build -t authentication_test -f authentication_test/Dockerfile_authentication .
docker build -t authorization_test -f authorization_test/Dockerfile_authorization .
docker build -t content_test -f content_test/Dockerfile_content .

# Run docker-compose
docker-compose up --abort-on-container-exit

# Save logs
docker-compose logs > log.txt


