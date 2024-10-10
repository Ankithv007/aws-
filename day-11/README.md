# AWS CloudFormation (CFT) Guide

## Overview

**AWS CloudFormation (CFT)** is an Infrastructure as Code (IaC) service provided by Amazon Web Services (AWS). It enables you to define and provision your cloud infrastructure in a simple text file (JSON or YAML format) to automate the creation and management of AWS resources. Using CloudFormation, you can model, set up, and manage a collection of related AWS resources, provisioning them in an orderly and predictable manner.

## Why Use CloudFormation?

- **Infrastructure as Code**: Manage your infrastructure using code, making it easy to version control and automate changes.
- **Automated Resource Management**: Automatically create, update, and delete AWS resources based on predefined templates.
- **Consistency and Reproducibility**: Ensure consistent configurations across environments, reducing human error.
- **Resource Dependency Management**: CloudFormation automatically handles resource dependencies, ensuring resources are created in the correct order.
- **Rollback and Error Handling**: Supports automatic rollback on failure, ensuring resources are left in a consistent state.
- **Cost Management**: Easily track and manage costs for the resources defined in a CloudFormation stack.

## Key Concepts in CloudFormation

### Stack

A stack is a collection of AWS resources that you can manage as a single unit. You create, update, and delete a collection of resources by creating, updating, and deleting stacks.

### Template

A CloudFormation template is a text file written in JSON or YAML format that defines the AWS resources to be created, such as EC2 instances, S3 buckets, and VPCs.

### Stack Set

Allows you to create, update, or delete stacks across multiple AWS accounts and regions with a single operation.

### Change Set

A preview of the changes CloudFormation will apply when you update a stack, allowing you to see how your template changes will affect your existing resources before actually making changes.

### Resource

An AWS service or infrastructure component, such as an EC2 instance, S3 bucket, or RDS database, defined in a CloudFormation template.

### Parameters

Parameters are used to pass values to your template at runtime. They enable you to customize your stack without changing the template.

### Mappings

Static variables within the template that you can use to define key-value pairs, such as region-specific AMI IDs.

### Outputs

Values returned after the stack is created. Outputs can be used as input values for other stacks or to reference resources.

## CloudFormation Template Structure

A typical CloudFormation template is structured with several key sections:
- for first it is t2.micro go stop and change the insatnce type into t2.medium it will drift the detection
- change the ami id and pem key
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: A sample CloudFormation template that creates an EC2 instance with SSH access.

Parameters:
  InstanceType:
    Description: Enter the EC2 instance type
    Type: String
    Default: t2.micro

  KeyPairName:
    Description: Enter the name of an existing EC2 Key Pair to enable SSH access to the instance.
    Type: AWS::EC2::KeyPair::KeyName
    Default: jaya  # Set the default value to your key pair name
    ConstraintDescription: Must be the name of an existing EC2 Key Pair.

Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: !Ref InstanceType  # Referring to the InstanceType parameter
      ImageId: ami-0dee22c13ea7a9a67  # Your specified AMI ID
      KeyName: !Ref KeyPairName  # Referring to the KeyPairName parameter

Outputs:
  InstanceId:
    Description: The Instance ID of the created EC2 instance
    Value: !Ref MyEC2Instance  # Referring to the EC2 instance resource


```
# Infrastructure as Code (IaC) Tools Comparison

## CloudFormation (CFT)
AWS CloudFormation is a service that allows you to define and provision AWS infrastructure using a declarative template format (JSON or YAML). 

### Pros:
- **AWS Integration**: Native support for AWS services, ensuring compatibility and security.
- **Managed Service**: Fully managed by AWS, reducing overhead for maintenance.
- **Rollback Capabilities**: Supports stack rollback on failure, ensuring stability.

### Cons:
- **Limited to AWS**: Only works with AWS services, limiting cross-cloud capabilities.
- **Complexity in Large Deployments**: Can become cumbersome and complex for large environments.

## Terraform
Terraform is an open-source IaC tool that enables you to build, change, and version infrastructure safely and efficiently. It supports multiple cloud providers, making it a versatile choice.

### Pros:
- **Multi-Cloud Support**: Can manage infrastructure across various cloud providers (AWS, Azure, Google Cloud, etc.).
- **Modular Approach**: Encourages a modular design through reusable modules, promoting best practices.
- **State Management**: Maintains a state file, providing insights into resource changes and current infrastructure.

### Cons:
- **Learning Curve**: Requires learning the HashiCorp Configuration Language (HCL), which may be unfamiliar to some users.
- **State File Management**: Managing state files, especially in team environments, can introduce complexity.

## AWS Cloud Development Kit (CDK)
AWS CDK is an open-source software development framework that allows you to define cloud infrastructure using familiar programming languages like JavaScript, Python, Java, and C#.

### Pros:
- **Programming Language Support**: Leverages the power of general-purpose programming languages, enabling complex logic in infrastructure definitions.
- **Abstraction**: Provides higher-level abstractions over AWS resources, making it easier to work with.
- **Rapid Development**: Allows for faster development cycles with the use of constructs and libraries.

### Cons:
- **AWS Specific**: Primarily focused on AWS, similar to CloudFormation.
- **Less Mature**: While rapidly evolving, it may not have all features and stability compared to Terraform or CloudFormation.

## Summary
- **Use CloudFormation** if you are deeply integrated into the AWS ecosystem and need a fully managed service for AWS resources.
- **Choose Terraform** for multi-cloud deployments and greater flexibility with a focus on modularity.
- **Opt for AWS CDK** if you prefer using programming languages to define your infrastructure and need higher-level abstractions.

#### To create an AWS CloudFormation template that allows the user to provision EC2 instances with specific instance types (t2.micro, t2.nano, and t2.medium) and gives permissions to create an S3 bucket, while also monitoring for drift,
#### To allow users to create their own EC2 key pair and specify their own S3 bucket name manually, you can modify the CloudFormation template. The updated template will include parameters for both the S3 bucket name and EC2 key pair,
```
AWSTemplateFormatVersion: '2010-09-09'
Description: CloudFormation template to create an EC2 instance with restricted types and user-defined S3 bucket name and EC2 key pair.

Parameters:
  InstanceType:
    Description: Choose the EC2 instance type (only t2.micro, t2.nano, and t2.medium are allowed)
    Type: String
    Default: t2.micro
    AllowedValues:
      - t2.micro
      - t2.nano
      - t2.medium
    ConstraintDescription: Must be one of the following instance types: t2.micro, t2.nano, t2.medium.

  BucketName:
    Description: Enter a unique name for your S3 bucket
    Type: String
    MinLength: 3
    MaxLength: 63
    AllowedPattern: '^[a-z0-9.-]*$'  # Only lowercase letters, numbers, and hyphens allowed.
    ConstraintDescription: Must be a unique bucket name (lowercase letters, numbers, and hyphens only).

  KeyPairName:
    Description: Enter the name of an existing EC2 Key Pair to enable SSH access to the instance.
    Type: AWS::EC2::KeyPair::KeyName
    ConstraintDescription: Must be the name of an existing EC2 Key Pair.

Resources:
  # S3 Bucket
  MyS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Ref BucketName

  # EC2 Instance
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: !Ref InstanceType  # Use the selected instance type
      ImageId: ami-0dee22c13ea7a9a67  # Replace with a valid AMI ID for your region
      KeyName: !Ref KeyPairName  # Use the specified key pair name
      SecurityGroupIds:
        - !Ref MySecurityGroup  # Reference the security group

  # Security Group
  MySecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow SSH access
      VpcId: vpc-xxxxxxx  # Replace with your VPC ID
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0  # Allow SSH from anywhere (use caution)

Outputs:
  InstanceId:
    Description: The Instance ID of the created EC2 instance
    Value: !Ref MyEC2Instance

  S3BucketName:
    Description: The name of the created S3 bucket
    Value: !Ref MyS3Bucket
```
```
AWSTemplateFormatVersion: '2010-09-09'
Description: CloudFormation template to create an EC2 instance with restricted types and S3 bucket permissions.

Parameters:
  InstanceType:
    Description: Choose the EC2 instance type (only t2.micro, t2.nano, and t2.medium are allowed)
    Type: String
    Default: t2.micro
    AllowedValues:
      - t2.micro
      - t2.nano
      - t2.medium
    ConstraintDescription: Must be one of the following instance types: t2.micro, t2.nano, t2.medium.

  BucketName:
    Description: Enter a unique name for your S3 bucket
    Type: String

Resources:
  # S3 Bucket
  MyS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Ref BucketName

  # EC2 Instance
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: !Ref InstanceType  # Use the selected instance type
      ImageId: ami-0dee22c13ea7a9a67  # Replace with a valid AMI ID for your region
      KeyName: my-key-pair  # Replace with your EC2 Key Pair
      SecurityGroupIds:
        - !Ref MySecurityGroup  # Reference the security group

  # Security Group
  MySecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow SSH access
      VpcId: vpc-xxxxxxx  # Replace with your VPC ID
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0  # Allow SSH from anywhere (use caution)

Outputs:
  InstanceId:
    Description: The Instance ID of the created EC2 instance
    Value: !Ref MyEC2Instance

  S3BucketName:
    Description: The name of the created S3 bucket
    Value: !Ref MyS3Bucket
```


