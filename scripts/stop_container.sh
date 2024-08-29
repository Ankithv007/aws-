#!/bin/bash
set -e

# Print a message to indicate script execution
echo "Stopping container..."

# Stop the running container (if any) and remove it
container_id=$(docker ps -q --filter "ancestor=ankithbv007/simple-python-flask-app")

if [ -n "$container_id" ]; then
  echo "Stopping and removing container ID: $container_id"
  docker rm -f $container_id
else
  echo "No running container found with the image 'ankithbv007/simple-python-flask-app'."
fi

# Start a new container with the same image
echo "Starting a new container..."
docker run -d ankithbv007/simple-python-flask-app

# Verify if the container is running
new_container_id=$(docker ps -q --filter "ancestor=ankithbv007/simple-python-flask-app")

if [ -n "$new_container_id" ]; then
  echo "New container started successfully with ID: $new_container_id"
else
  echo "Failed to start a new container."
fi
