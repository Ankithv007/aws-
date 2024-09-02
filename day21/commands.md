### To create a Docker setup that includes your Dockerfile, app.py, and requirements.txt in a single directory and then build and push the Docker image to an Amazon ECR repository, follow these steps:

# Login to ECR (replace <region> and <account-id> with your actual values)
$ aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com

# Build the Docker image (replace <repo-name> with your ECR repository name)
$ docker build -t <account-id>.dkr.ecr.<region>.amazonaws.com/<repo-name>:latest .

# Push the Docker image to ECR (replace <repo-name> with your ECR repository name)
$ docker push <account-id>.dkr.ecr.<region>.amazonaws.com/<repo-name>:latest

 ######
1. - login command you can copy from ECR
2. - To build --Copy of half(docker build -t 014498645710.dkr.ecr.ap-south-1.amazonaws.com:latest .)
3. - To push  --Copy of full(docker push 014498645710.dkr.ecr.ap-south-1.amazonaws.com/sample-app:latest)
