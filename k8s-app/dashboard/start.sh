# 生成管理 DashBoard 的账户
kubectl apply -f dashboard-admin.yaml 

# 查看 Token
kubectl describe secrets -n kube-system dashboard-admin-token-x2qkv