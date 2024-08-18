<h4> change the ami and subnet keypair and sg  accoring to the vpc </h4>

<h4> to describe and for checking aim</h4>
aws ec2 describe-images \
    --owners amazon \
    --filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" \ 
    --query "Images[*].[ImageId,Name]" \
    --output table

<h5> check and use it when creating the ec2</h5>
 aws ec2 describe-images --image-ids ami-03c3ac54a88879408  //change the emi according to the log

<h4> change the ami and subnet keypair and sg  accoring to the vpc (while taking take as a raw code)</h4> 
 aws ec2 run-instances \
    --region ap-south-1 \
    --image-id ami-03c3ac54a88879408 \
    --instance-type t2.micro \
    --key-name MyKeyPair \
    --security-group-ids sg-05efc9f1faa23ef15 \
    --subnet-id subnet-019675d33edf924c7 \
    --associate-public-ip-address \
    --block-device-mappings '[{"DeviceName":"/dev/sda1","Ebs":{"VolumeSize":8}}]' \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=MyInstance}]' \
    --count 1

aws ec2 run-instances     --region ap-south-1     --image-id ami-03c3ac54a88879408     --instance-type t2.micro     --key-name MyKeyPair     --security-group-ids sg-05efc9f1faa23ef15     --subnet-id subnet-019675d33edf924c7     --associate-public-ip-address     --block-device-mappings '[{"DeviceName":"/dev/sda1","Ebs":{"VolumeSize":8}}]'     --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=MyInstance}]'     --count 1

