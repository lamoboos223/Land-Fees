from kafka import KafkaProducer


class Producer:

    def __init__(self):
        self.TOPIC = "LandsFee"
        self.bootstrap_servers = "localhost:9092"
        self.encode = "utf-8"

    def produce(self, value):
        value = str(value)
        kafka_producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                       value_serializer=lambda x: (x.encode(self.encode)))

        kafka_producer.send(self.TOPIC, value=value)
        print("Value: %s sent to topic: %s" % (value, self.TOPIC))

        kafka_producer.flush()
        kafka_producer.close()
