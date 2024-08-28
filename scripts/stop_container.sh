#!/bin/bash
set -e

# Print a message to indicate script execution
echo "Stopping container..."

# Stop the running container (if any)
container_id=$(docker ps -q --filter "ancestor=ankithbv007/simple-python-flask-app")

if [ -n "$container_id" ]; then
  echo "Stopping and removing container ID: $container_id"
  docker rm -f $container_id
else
  echo "No running container found with the image 'ankithbv007/simple-python-flask-app'."
fi
