1. 09277 박한주

kafka-topics --create \
--zookeeper localhost:2181 \
--replication-factor 1 \
--partitions 1 \
--topic weblogs

kafka-topics --list \
--zookeeper localhost:2181

kafka-topics --describe weblogs \
--zookeeper localhost:2181

kafka-console-producer \
--broker-list localhost:9092 \
--topic weblogs

kafka-console-consumer \
--zookeeper localhost:2181 \
--topic weblogs \
--from-beginning
