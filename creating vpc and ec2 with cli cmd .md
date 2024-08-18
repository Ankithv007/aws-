<h1>Creating a VPC</h1>
aws ec2 create-vpc --cidr-block 10.0.0.0/16

<h1>Creating Subnets</h1>
aws ec2 create-subnet --vpc-id <vpcId> --cidr-block 10.0.1.0/24
aws ec2 create-subnet --vpc-id <vpcId> --cidr-block 10.0.2.0/24  //vpc id shld add after

<h1>Creating Internet Gateway</h1>
aws ec2 create-internet-gateway
aws ec2 attach-internet-gateway --vpc-id <vpcId> --internet-gateway-id <InternetGatewayId>  //to attach to vpc and igw

<h1>Creating Route Table</h1>
aws ec2 create-route-table --vpc-id <vpcId>
  
aws ec2 create-route --route-table-id <RouteTableId> 
              --destination-cidr-block 0.0.0.0/0 --gateway-id <internetGatewayId> 
              
<h1>Viewing the Route Table and Subnets</h1>
aws ec2 describe-route-tables --route-table-id <RouteTableId>

aws ec2 describe-subnets --filters "Name=vpc-id,Values=<vpcId>"
                         --query "Subnets[*].{ID:SubnetId,CIDR:CidrBlock}"


<h1> Associating Route Table and modifying subnet</h1>
aws ec2 associate-route-table --subnet-id <SubnetId> --route-table-id <RouteTableId>

aws ec2 modify-subnet-attribute --subnet-id <SubnetId> --map-public-ip-on-launch

<h1> Creating Key Pair  </h1>
aws ec2 create-key-pair --key-name MyKeyPair --query "KeyMaterial" --output text > ~/MyKeyPair.pem


<h1>For security group use the below commands </h1>
                                    
aws ec2 create-security-group --group-name <security-group-name> --description "<description>"
                              --vpc-id <vpcId>

aws ec2 authorize-security-group-ingress --group-id <GroupId> 
                                         --protocol tcp --port 22 --cidr 0.0.0.0/0


<h1> Running the EC2 Instance </h1>
aws ec2 run-instances --image-id <ami-id> --count 1 --instance-type t2.micro 
                      --key-name <Keypair-name> --security-group-ids <SecurityGroupId> 
                      --subnet-id <SubnetId>

 <h3> for ami id  </h3> 
          aws ec2 describe-images \
    --owners amazon \
    --filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" \
    --query "Images[*].[ImageId,Name]" \
    --output table

aws ec2 describe-images --image-ids  <  // give any ami id to verify//      ami-0abcdef1234567890 >

    


<h1> Viewing the Instance </h1>
aws ec2 describe-instances --instance-id <InstanceId>

<h1> Verifying the EC2 Instance </h1>
Go and verify with your ui (user insterface account)



                        


