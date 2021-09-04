import MOJ
import Balady
import db
import KafkaClient

moj_api = MOJ.MOJAPI()
balady_api = Balady.FasehAPI()
mysqldb = db.mysqldb()
kafka_producer = KafkaClient.Producer()

land_info = moj_api.getOwnerData("1996", "2021")
print(land_info)
identity_number = land_info["identity_number"]
instrument_number = land_info["instrument_number"]
spaces = moj_api.getOwnerMeters(identity_number, "Riyadh")["spaces"]
if spaces >= 5000:
    isValid = balady_api.isValid(instrument_number)
    if isValid:
        count = mysqldb.isExists(identity_number, instrument_number)
        if count > 0:
            mysqldb.add(identity_number, instrument_number)
            kafka_producer.produce(land_info)
