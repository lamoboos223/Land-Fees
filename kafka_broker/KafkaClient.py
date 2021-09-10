from kafka import KafkaProducer, KafkaConsumer
import json


class Producer:

    def __init__(self):
        self.TOPIC = "NOTIFIED_USERS"
        self.bootstrap_servers = "localhost:9092"
        self.encode = "utf-8"

    def produce(self, value):
        # this is for the jdbc sink to work cause it doesn't know how to parse json without a schema
        value = '''
        {"schema":
                 {
                     "type": "struct", "optional": "false", "version": 1, "fields":
                     [
                         {"field": "land_number",
                             "type": "string", "optional": "true"},
                         {"field": "block_number",
                             "type": "string", "optional": "true"},
                         {"field": "instrument_number",
                             "type": "string", "optional": "true"},
                         {"field": "identity_number",
                             "type": "string", "optional": "true"},
                         {"field": "first_name", "type": "string", "optional": "true"},
                         {"field": "last_name", "type": "string", "optional": "true"},
                         {"field": "mobile", "type": "string", "optional": "true"},
                         {"field": "email", "type": "string", "optional": "true"},
                         {"field": "purchased_fee",
                             "type": "string", "optional": "true"},
                         {"field": "land_space", "type": "int64", "optional": "true"}
                     ]
                 },
                 "payload": %s
                 }
        ''' % value
        kafka_producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                       value_serializer=lambda x: x.encode("utf-8"))
        kafka_producer.send(self.TOPIC, value=value)
        kafka_producer.flush()
        kafka_producer.close()

    def dummyProducer(self, value):
        kafka_producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                       value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        kafka_producer.send('WhiteLands', value=json.dumps(value))
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
            value_deserializer=lambda x: json.loads(x.decode("utf-8")))
        return consumer
