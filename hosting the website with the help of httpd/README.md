<h1> hii everyone! </h1>
<br>
creating of vpc with cidr depending our ip adress how much we need for the system and for the subnets
<br>
<br>
create and attach to the igw
create the route table as of now we use a pub-rt and choose the vpc what we have crated earlier not a defalut one
<br>
create the subenet adn choose the avalabilty zone and attach to vpc  split ip adress according to your requirement 
<br>
and go agin to route table attach the igw means route and do subnet assicaiation in the route table configuration
<br>
here we can end the vpc part 
or else you can choose the dafault vpc that is also ok thats give entire thing to us from sg ,sunbet,route table ,igw
<br>
<h1> installation of EC2 </h1>
here we have to choose linux distribution 
in my case i use amazon linuxx
note each disrtibution have thier own command 

after chooseing we have to give the key pair value to acess 
<br>
after all set we have acess the vm in any 3rd party app like mobaxtream,putty,or in the cmd promt
<br>
here we have update the ec2 machine first for that
we write the linux command 
 first to beacome  a root user we use this command
 sudo su ,sudi -i
 <br>
 to update ec2 machine
<br>
yum update 
<br>
for chaning directory
cd/ 
ls(list)
cd var
pwd (preset working dir)
cd www
pwd
cd html
touch index.html (open the file)
in this file add some html cose to  show up in web browser
cat index.html (view the file)
vim index.html (edit the file)

<br>
to install the apache server or httpd 
systemctl start httpd -y
systemctl enable httpd -y 
systemctl status httpd -y (to check the status)
systemctl stop httpd -y (to stop)

after this step up
in the security group we have give the promission to access for the http or for https in the case of if we go with default vpc
<br>
after this all set copy your public ip adress and paste it in web your application will run 






