import pulsar

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('persistent://public/default/RawData', subscription_name='rawdata-subscriber')

try:
    while True:
        msg = consumer.receive()
        print(f"Received: '{msg.data().decode('utf-8')}'")
        consumer.acknowledge(msg)
finally:
    client.close()
