1.  kubectl installation
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/kubectl
```

2.eks installation 
```
# for ARM systems, set ARCH to: `arm64`, `armv6` or `armv7`
ARCH=amd64
PLATFORM=$(uname -s)_$ARCH

curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"

# (Optional) Verify checksum
curl -sL "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_checksums.txt" | grep $PLATFORM | sha256sum --check

tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz

sudo mv /tmp/eksctl /usr/local/bin
```

3.  for check to that has install eks
```
eksctl
```
4. install aws cli
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip

sudo ./aws/install

aws --version

aws configure
```
5. Create a eks cluster
```
eksctl create cluster --name demo-cluster-2 --region ap-south-1 --fargate
```
6.to get the all resources from cluster to the cli not in ui 
```
 aws eks update-kubeconfig --name demo-cluster-1  --region ap-south-1
```
7. create forgate profile
```
eksctl create fargateprofile \
    --cluster demo-cluster \
    --region us-east-1 \ 
    --name alb-sample-app \
    --namespace game-2048
```

8.add the application service ingress and also deployement
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.4/docs/examples/2048/2048_full.yaml
```
9.IAM OIDC provider configured -this is pre requisite for alb controller  (to add the ingress controller) (in ui there oide provider in authentication tab )
```
eksctl utils associate-iam-oidc-provider --cluster demo-cluster-1 --approve
```
10. install alb ingress controller ( this also pod we will give access to AWS service 	such as ALB) (we create IAM polices and rule)
- Download IAM policy
```
curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.4/docs/install/iam_policy.json
```
- Create IAM Policy (if it already leave it else go to IAM and delete with this AWSLoadBalancerControllerIAMPolicy name)
```
aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam_policy.json
```
-Create IAM Role (change the cluster name ,account-id,) ( last line if practicing twice in one account and also change load balancer name)
```
eksctl create iamserviceaccount \
  --cluster=<your-cluster-name> \
  --namespace=kube-system \
  --name=aws-load-balancer-controller-1 \
  --role-name AmazonEKSLoadBalancerControllerRole \
  --attach-policy-arn=arn:aws:iam::<your-aws-account-id>:policy/AWSLoadBalancerControllerIAMPolicy \
  --approve \
  --override-existing-serviceaccounts

```
11.Deploy ALB controller
```
# Update the package list
sudo apt update

# Install the required packages
sudo apt install apt-transport-https ca-certificates curl -y

# Install Helm
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

```
- helm update
```
 helm repo add eks https://aws.github.io/eks-charts
```
```
helm repo update eks

```
12.insatll helm chart with add vpc many  more( take vpc id in eks networking)(if indeteation comes go to chat gpt and add this)
```
helm install aws-load-balancer-controller eks/aws-load-balancer-controller -n kube-system \
  --set clusterName=demo-cluster-2 \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller-v5 \
  --set region=ap-south-1 \
  --set vpcId=vpc-0eac1c8ce90f74f87

```
- to check to that the load balancer is ready ( if it not come out trouble shoot this)
```
 kubectl get deployment -n kube-system aws-load-balancer-controller
```
```
kubectl get deployment -n kube-system 
```
```
kubectl get pods -n kube-system
```
- for get ingrees this in game-2048 name sapce
```
kubectl get ingress -n game-2048
```
- and ingress controller created this adress (go and check in ec2 dashboard load balancer (in lb DNS name it is the same ip that provide in ingress controller also))
```
  k8s-game2048-ingress2-fe2829f6d9-185779879.ap-south-1.elb.amazonaws.com
```
- and get the link from the load balancer only and acces through web









