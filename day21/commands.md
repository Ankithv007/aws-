### To create a Docker setup that includes your Dockerfile, app.py, and requirements.txt in a single directory and then build and push the Docker image to an Amazon ECR repository, follow these steps:

# Login to ECR (replace <region> and <account-id> with your actual values)
$ aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com

# Build the Docker image (replace <repo-name> with your ECR repository name)
$ docker build -t <account-id>.dkr.ecr.<region>.amazonaws.com/<repo-name>:latest .

# Push the Docker image to ECR (replace <repo-name> with your ECR repository name)
$ docker push <account-id>.dkr.ecr.<region>.amazonaws.com/<repo-name>:latest
