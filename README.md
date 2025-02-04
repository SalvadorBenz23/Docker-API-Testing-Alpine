# Exam

This repository contains the exam project for testing Docker containers. The project aims to validate the functionality of a CI/CD pipeline for testing an API using Docker containers.

## Directory Structure

The exam directory structure is as follows:

exam/
│
├── authentication_test/
│ ├── Dockerfile
│ ├── authentication_test.py
│
├── authorization_test/
│ ├── Dockerfile
│ ├── authorization_test.py
│
├── content_test/
│ ├── Dockerfile
│ ├── content_test.py
│
├── docker-compose.yml
├── log.txt
└── logs_volume.txt
└── README.md
└── setup.sh


## Setup.sh

The project utilizes Docker containers for testing the API. The setup.sh script builds Docker images for authentication_test, authorization_test, and content_test using the respective Dockerfiles in their directories. Then, it runs docker-compose to orchestrate the execution of the test containers. Finally, it saves the logs from the test containers into a log.txt file.

## Notes on Setup.sh

A few lines are commented-out on the setup.sh file and can be used for setting up the environment. Make sure you uncomment before executing especially if used from a new machine:

- **Docker Image Pull**: If needed, you can uncomment the lines for pulling the Docker image `datascientest/fastapi:1.0.0` at the beginning of the script.

````console
#docker image pull datascientest/fastapi:1.0.0
````

- **Docker Volume Creation**: Similarly, if you want to use a Docker volume for storing the test scripts (`authentication_test.py`, `authorization_test.py`, `content_test.py`), you can uncomment the line for creating the Docker volume. The dockerfile of each container should copy the content of the directory but I encourage you to still create a volume and perform these cp commands at once for a successful test.

````console
#docker volume create api_test
````

- **sudo cp -v**: Once your volume is created, you will want to put the test scipts in these folders in order to transmit it to your containers upon booting, so that the test scripts can execute.

````console
#sudo cp -v authentication_test/authentication_test.py /var/lib/docker/volumes/api_test/_data
#sudo cp -v authorization_test/authorization_test.py /var/lib/docker/volumes/api_test/_data
#sudo cp -v content_test/content_test.py /var/lib/docker/volumes/api_test/_data
````

## Choice of Docker Images

Initially, there were complications in installing Python packages within Docker containers using the traditional Python runtime images. To address this issue, I opted for Alpine-based Python images, which are lightweight and already had most packages already installed. This choice helped streamline the Docker image building process and reduce image size.

## Logging

Two log files are generated during the test execution:

- log.txt: Contains the output of the docker-compose command, capturing the overall execution process and any errors encountered.
- logs_volume.txt (api_test.log copy): A cleaner log file generated from a volume mounted on the test containers at execution time. Each container writes its test results to this file. This log provides detailed information about the individual test outcomes using the `cat /var/lib/docker/volumes/api_test/_data/api_test.log `command.

These logs serve as valuable records of the test execution process, aiding in troubleshooting and analysis.

## Tests

```python
print("============================")
print("    Authentication Test")
print("    Authorization Test")
print("    Content Test"    )   
print("============================")

```

1. The `authentication_test.py` script sends a GET request to the /permissions endpoint of the API with predefined username and password parameters ('alice' and 'wonderland' respectively). It then checks the response status code: if it's 200, the test is considered successful; otherwise, it's marked as a failure. 

2. The `authorization_test.py` script conducts authorization testing by sending GET requests to both the /v1/sentiment and /v2/sentiment endpoints for multiple users with different versions. It iterates through predefined user data containing usernames, passwords, and versions. For each user and version combination, it sends a request and checks the response status code. 

3. The `content_test.py` script performs content testing by sending GET requests to the /v1/sentiment endpoint with predefined test sentences for a specific user. It iterates through the test sentences, sends requests, and extracts sentiment scores from the response. Based on the sentiment score, it determines whether the sentiment is positive or negative and compares it with the expected sentiment. 

The test results are displayed and written in a log.txt file.

Additionally, if the LOG environment variable is set, the test results are written to a log file named api_test.log on a pre-mounted volume.

## Possible Improvements

Some ideas:

1. Setting a bash command to retrieve clean logs from the volume.

2. Deleting the volume once the tests are done. 

3. Creating a new volume for containers each time they are instantiated.

4. The tests can be managed remotely with an orchestration server (like Kubernetes) and be triggered semi-automatically, for exemple when a new software release must be tested, i.e. pre-release. The whole tests can be monitored from a central dashboard and various reports are created.


Feel free to reach out if you have any questions or suggestions for improvements!

