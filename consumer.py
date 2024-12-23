# to initiate the code, do the following steps (the steps must run in order):
# 1. Open a kafka file in terminal
# 2. Run .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
# 3. Run .\bin\windows\kafka-server-start.bat .\config\server.properties
# 4. Run python consumer.py

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'my_topic',
    bootstrap_servers=['localhost:9092'],
    api_version=(0, 10),
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    group_id='my_group_id',
    value_deserializer=lambda x: x.decode('utf-8')
)

print("Consumer is listening...")

for message in consumer:
    print("Received message: ", message.value)
