helm repo add apache https://pulsar.apache.org/charts
helm repo update

kubectl taint nodes desktop-master node-role.kubernetes.io/master-



helm install pulsar apache/pulsar \
  --version 3.9.0 \
  -f values.yaml -n pulsar