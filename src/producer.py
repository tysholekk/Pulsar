import pulsar
import time

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('persistent://public/default/RawData')

try:
    while True:
        message = f"Sensor reading at {time.time()}"
        producer.send(message.encode('utf-8'))
        print(f"Sent: {message}")
        time.sleep(1)
finally:
    client.close()
