# AWS CLI Guide

## Overview

The **AWS Command Line Interface (CLI)** is a unified tool to manage and automate AWS cloud services. It allows users to interact with AWS services through commands in their terminal or command prompt, making it easier to script operations and integrate AWS services into existing workflows. The CLI is especially useful for automating repetitive tasks, managing resources programmatically, and controlling cloud infrastructure without the need for the AWS Management Console.

### Why Use AWS CLI?

- **Automation**: AWS CLI supports automation of tasks such as deploying applications, managing infrastructure, and configuring settings using shell scripts or batch files.
- **Control**: Directly execute AWS service commands and API actions from your command line.
- **Flexibility**: Supports complex operations, filtering, and output formatting options.
- **Integration**: Easily integrate with other tools and scripts, making it an ideal choice for CI/CD pipelines and infrastructure-as-code (IaC) setups.

## Prerequisites

Before starting with AWS CLI, ensure you have:

- An **AWS Account** with an active subscription.
- An **IAM user** with the necessary permissions for using AWS CLI commands.
- **AWS CLI installed** on your local machine.

## Installation
### Linux

Refer to the [installation steps](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html) for Linux distributions.

```
# 1. Install dependencies
sudo apt update && sudo apt install -y unzip curl

# 2. Download the latest AWS CLI v2 installer
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# 3. Unzip the installer
unzip awscliv2.zip

# 4. Run the install script
sudo ./aws/install

# 5. Verify the install
aws --version
```

## Configuration

Once the AWS CLI is installed, configure it

```
aws configure
```
