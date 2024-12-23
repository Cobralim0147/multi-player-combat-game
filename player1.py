from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"]
)

producer.send("my_topic", value="Hello, World!".encode("utf-8"))