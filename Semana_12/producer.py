# pip install confluent-kafka
from confluent_kafka import Producer

BROKERS = "kafka1:19092"  # kafka1:19092,kafka2:29092,kafka3:39092
TOPIC = "test"
MESSAGES = ["hola", "coder", "bienvenidos a kafka"]

p = Producer({"bootstrap.servers": BROKERS})


def delivery_report(err, msg):
    """Called once for each message produced to indicate delivery result.
    Triggered by poll() or flush()."""
    if err is not None:
        print("Message delivery failed: {}".format(err))
    else:
        print("Message delivered to {} [{}]".format(msg.topic(), msg.partition()))


for data in MESSAGES:
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message. The delivery report callback will
    # be triggered from the call to poll() above, or flush() below, when the
    # message has been successfully delivered or failed permanently.
    p.produce(TOPIC, data.encode("utf-8"), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()
