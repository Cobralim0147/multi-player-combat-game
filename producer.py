from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",  # Ensure it matches the consumer's broker
    api_version=(0, 10)
)

print("Sending message...")
producer.send("my_topic", value="Hullo".encode("utf-8"))  # Ensure topic name matches
print("Message sent!")
