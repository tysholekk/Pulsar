bin/pulsar-admin tenants list

bin/pulsar-admin tenants update public --allowed-clusters pulsar

bin/pulsar-admin topics list public/default

bin/pulsar-admin topics create-partitioned-topic persistent://public/default/RawData --partitions 3


pip install pulsar-client



kubectl port-forward svc/pulsar-proxy 6650:6650


helm dependency build


helm install pulsar -f my-values.yaml ./charts/pulsar