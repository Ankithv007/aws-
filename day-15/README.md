### Deployement 
#### Install the CodeDeploy agent for Ubuntu Server


- iam role creation and adding that into exsiting ec2
  ### AWS CLI and IAM User Setup Guide

## Prerequisites
Ensure you have access to an AWS account with the necessary permissions to create IAM users and roles.

## Step 1: Install AWS CLI

To install AWS CLI on Ubuntu, follow these commands:

```bash
# Download the AWS CLI installer
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# Install unzip if not already installed
sudo apt install unzip -y

# Unzip the installer
unzip awscliv2.zip

# Run the installer
sudo ./aws/install

# Verify the installation
aws --version

aws configure
```
```
# Create the IAM user
aws iam create-user --user-name CodeDeployUser

# Attach the AWSCodeDeployRole policy
aws iam attach-user-policy --user-name CodeDeployUser --policy-arn arn:aws:iam::aws:policy/service-role/AWSCodeDeployRole

# Attach EC2 Full Access policy
aws iam attach-user-policy --user-name CodeDeployUser --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess

```
### Remove Older AMIs (if necessary)
```
aws ec2 deregister-image --image-id <ami-id>

```
--------------------------------------------------------------------------------------------------------------------------------------------------------

# AWS CodeDeploy Agent Installation and IAM Setup Guide

## Prerequisites
- AWS CLI should be installed and configured on your machine.
- You should have an EC2 instance running Ubuntu.
- You should have sufficient IAM permissions to create roles, policies, and attach them to the instance.

---

## Step 1: Install the CodeDeploy Agent on Ubuntu Server

### 1.1 Update the Package List and Install Dependencies

```bash
# Update the package list
sudo apt update

# Install Ruby and Wget
sudo apt install ruby wget -y
```
#### Download and Install the CodeDeploy Agent
```
# Download the CodeDeploy agent installer from the S3 bucket for your region
cd /home/ubuntu
wget https://aws-codedeploy-ap-south-1.s3.ap-south-1.amazonaws.com/latest/install

# Make the install script executable
chmod +x ./install

# Run the install script
sudo ./install auto

```

#### Start and Enable the CodeDeploy Agent
```
# Start the CodeDeploy agent
sudo service codedeploy-agent start

# Enable the CodeDeploy agent to start on boot
sudo systemctl enable codedeploy-agent

```

#### Verify the CodeDeploy Agent Status
```
# Check if the CodeDeploy agent is running
sudo service codedeploy-agent status
```
