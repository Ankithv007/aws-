### To create a Docker setup that includes your Dockerfile, app.py, and requirements.txt in a single directory and then build and push the Docker image to an Amazon ECR repository, follow these steps:

# Login to ECR (replace <region> and <account-id> with your actual values)
```
$ aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
```
example
```
aws ecr get-login-password --region ap-south-1| docker login --username AWS --password-stdin 324037289876.dkr.ecr.ap-south-1.amazonaws.com

aws ecr get-login-password --region <change accordingly>| docker login --username AWS --password-stdin <when you create ecr(uri) it will give this copy paste from there until amazon.com not name>
```

# Build the Docker image (replace <repo-name> with your ECR repository name)
$ docker build -t <account-id>.dkr.ecr.<region>.amazonaws.com/<repo-name>:latest .
example
```
docker build -t 324037289876.dkr.ecr.ap-south-1.amazonaws.com/python-web-app:latest .

docker build -t <when you create ecr -->(uri) it will give this copy paste from there and add : version (like latest, v1,v2) .
```

# Push the Docker image to ECR (replace <repo-name> with your ECR repository name)
$ docker push <account-id>.dkr.ecr.<region>.amazonaws.com/<repo-name>:latest
example---> copy the build tag remove the . (current location) and remove -t tag and build write push instead build 
```
docker push 324037289876.dkr.ecr.ap-south-1.amazonaws.com/python-web-app:latest

```

 ######
1. - login command you can copy from ECR
2. - To build --Copy of half(docker build -t 014498645710.dkr.ecr.ap-south-1.amazonaws.com:latest .)
3. - To push  --Copy of full(docker push 014498645710.dkr.ecr.ap-south-1.amazonaws.com/sample-app:latest)
