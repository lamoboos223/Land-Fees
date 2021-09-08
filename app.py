from third_party_services import MOJ, Balady
from db import db
from kafka_broker import KafkaClient
import datetime
import ast


CITY = 'Riyadh'
METERS = 5000

moj_api = MOJ.MOJAPI()
balady_api = Balady.FasehAPI()
mysqldb = db.mysqldb()
kafka_producer = KafkaClient.Producer()
kafka_consumer = KafkaClient.Consumer()

# Consume WhiteLand topic
consumer = kafka_consumer.consume()
for message in consumer:
    try:
        land = ast.literal_eval(message.value)
        # get land info from MOJ API
        land_info = moj_api.getOwnerData(
            land["land_number"], land["block_number"])
        identity_number = land_info["identity_number"]
        instrument_number = land_info["instrument_number"]
        # check if the user is already notified and saved in DB
        count = mysqldb.isExists(identity_number, instrument_number)
        if count != 0:
            # get owner meters from MOJ API
            spaces = moj_api.getOwnerMeters(identity_number, CITY)["spaces"]
            if spaces >= METERS:
                # check if the land has fence clearence from Balady
                isValid = balady_api.isValid(instrument_number)
                if isValid:
                    # check if the fence clearence is within this year from Balady
                    issuedAt = balady_api.issuedAt(instrument_number)
                    if(issuedAt < datetime.datetime.now().year):
                        # this line is going to be replaced by mysql sink connector
                        # mysqldb.add(identity_number, instrument_number)
                        kafka_producer.produce(land_info)
        else:
            print(" the user already notified")
    except TypeError as e:
        pass
