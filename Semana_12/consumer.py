# pip install confluent-kafka
from confluent_kafka import Consumer


BROKERS = "kafka1:19092"  # kafka1:19092,kafka2:29092,kafka3:39092
TOPIC = "test"
CONSUMER_GROUP = "python-consumer-group"

c = Consumer(
    {
        "bootstrap.servers": BROKERS,
        "group.id": CONSUMER_GROUP,
        "auto.offset.reset": "earliest",
    }
)

c.subscribe([TOPIC])

print("Listening for messages in test...")

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print("Received message: {}".format(msg.value().decode("utf-8")))

c.close()
