bin/pulsar-admin tenants list

bin/pulsar-admin tenants update public --allowed-clusters pulsar

bin/pulsar-admin topics list public/default

bin/pulsar-admin topics create-partitioned-topic persistent://public/default/RawData --partitions 3


pip install pulsar-client



kubectl port-forward svc/pulsar-proxy 6650:6650


helm dependency build


helm install pulsar -f my-values.yaml ./charts/pulsar

kubectl exec -it pulsar-toolset-0 -n pulsar -- /pulsar/bin/pulsar-perf produce -r 50 -m 10000 persistent://public/default/RawData


kubectl exec -it pulsar-toolset-0 -n pulsar -- \
  /pulsar/bin/pulsar-perf produce \
  -r 50 -m 10000 \
  --stats-interval-seconds 1 \
  -u pulsar://pulsar-proxy.pulsar.svc.cluster.local:6650 \
  persistent://public/default/RawData


kubectl apply -f pulsar-python.yaml