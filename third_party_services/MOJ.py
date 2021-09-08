import json


class MOJAPI:

    def __init__(self):
        pass

    def getOwnerData(self, land_number, block_number):
        self.land_number = land_number
        self.block_number = block_number

        if land_number == "1996" and block_number == "2021":
            return json.load(open("../Land-Fees/third_party_services/data.json"))
        return None

    def getOwnerMeters(self, identity_number, city):
        if identity_number == "1234567890" and city == "Riyadh":
            return {"spaces": 7000}
        return {"spaces": 3000}
