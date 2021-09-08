from kafka import KafkaProducer, KafkaConsumer


class Producer:

    def __init__(self):
        self.TOPIC = "LandFees"
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


class Consumer:

    def __init__(self):
        self.TOPIC = "WhiteLands"
        self.bootstrap_servers = "localhost:9092"
        self.encode = "utf-8"
        self.auto_offset_reset = 'earliest'
        self.group_id = 'group1'

    def consume(self):
        consumer = KafkaConsumer(
            self.TOPIC,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset=self.auto_offset_reset,
            group_id=self.group_id,
            value_deserializer=lambda x: (x.decode(self.encode)))

        return consumer
