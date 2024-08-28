#!/bin/bash
set -e

# Stop the running container (if any)
container_id=$(docker ps -q --filter "name=my-container")

if [ -n "$container_id" ]; then
  echo "Stopping and removing container ID: $container_id"
  docker rm -f $container_id
else
  echo "No running container found with the name 'my-container'."
fi
