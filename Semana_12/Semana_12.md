# Kafka in Docker
Kowl + Kafka + Zookeeper


# Kafka commands
```bash
// create topic
kafka-topics --create --bootstrap-server kafka1:9092 --topic test --partitions 3 --replication-factor 1

// list topics
kafka-topics --list --bootstrap-server kafka1:9092

// delete topic
kafka-topics --delete --bootstrap-server kafka1:9092 --topic test

// consumer group
docker exec -it semana_12-kafka1-1 bash
kafka-console-consumer --bootstrap-server kafka1:9092 --topic test --group terminal-consumer-group --from-beginning

// producer
docker exec -it semana_12-kafka1-1 bash
kafka-console-producer --broker-list kafka1:9092 --topic test
```