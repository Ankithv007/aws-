1.for eksctl
```
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_Linux_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin

```
- create cluster  (it will take like 20 min )
``` 
eksctl create cluster --name demo-cluster --region ap-south-1 --fargate
```
- create forgate profile
```
eksctl create fargateprofile \
    --cluster demo-cluster \
    --region ap-south-1 \
    --name alb-sample-app \
    --namespace game-2048
```

- Deploy the deployment, service and Ingress
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.4/docs/examples/2048/2048_full.yaml

```
- Check if there is an IAM OIDC provider configured already
```
eksctl utils associate-iam-oidc-provider --cluster $cluster_name --approve
eksctl utils associate-iam-oidc-provider --cluster <your cluster name> --approve

```

- How to setup alb add on
- Download IAM policy
```
curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.4/docs/install/iam_policy.json
```

- Create IAM Policy
```
aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam_policy.json
```
- Create IAM Role (change cluster name and your acc no)
```
eksctl create iamserviceaccount \
  --cluster=<your-cluster-name> \
  --namespace=kube-system \
  --name=aws-load-balancer-controller \
  --role-name AmazonEKSLoadBalancerControllerRole \
  --attach-policy-arn=arn:aws:iam::<your-aws-account-id>:policy/AWSLoadBalancerControllerIAMPolicy \
  --approve
```

- helm install
```
helm repo add eks https://aws.github.io/eks-charts
```
- helm update
```
helm repo update eks
```
```
helm install aws-load-balancer-controller eks/aws-load-balancer-controller -n kube-system \
  --set clusterName=demo-cluster \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller \
  --set region=ap-south-1 \ 
  --set vpcId=vpc-07812462b1b1a3488
````


- check this after the deployment  working  (load balancer will be create go ec2 dash board and check for lb)
```
kubectl get deployment -n kube-system aws-load-balancer-controller
```

-to verify the address
```
kubectl get ingress -n game-2048
```