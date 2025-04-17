helm repo add apache https://pulsar.apache.org/charts
helm repo update

helm install pulsar apache/pulsar \
  --version 3.9.0 \
  -f values.yaml