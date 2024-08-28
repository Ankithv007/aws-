#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull ankithbv007/simple-python-flask-app

# Run the Docker image as a container
docker run -d -p 5-000:5000  ankithbv007/simple-python-flask-app