# How to setup alb add on

Download IAM policy

```
curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.4/docs/install/iam_policy.json
```

Create IAM Policy

```
aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam_policy.json
```

Create IAM Role (change the cluster name ,account-id,)

```
eksctl create iamserviceaccount \
  --cluster=<your-cluster-name> \
  --namespace=kube-system \
  --name=aws-load-balancer-controller \
  --role-name AmazonEKSLoadBalancerControllerRole \
  --attach-policy-arn=arn:aws:iam::<your-aws-account-id>:policy/AWSLoadBalancerControllerIAMPolicy \
  --approve
```

## Deploy ALB controller

Add helm repo

```
helm repo add eks https://aws.github.io/eks-charts
```

Update the repo

```
helm repo update eks
```

Install (change vpc,region,name )
```
helm install aws-load-balancer-controller eks/aws-load-balancer-controller -n kube-system \
  --set clusterName=demo-cluster \<change here>
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller \
  --set region=ap-south-1 \ <change here>
  --set vpcId=vpc-07812462b1b1a3488<change here>

```

```
helm install aws-load-balancer-controller eks/aws-load-balancer-controller -n kube-system \
  --set clusterName=demo-cluster \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller \
  --set region=ap-south-1 \ 
  --set vpcId=vpc-07812462b1b1a3488
```

Verify that the deployments are running.

```
kubectl get deployment -n kube-system aws-load-balancer-controller
```


