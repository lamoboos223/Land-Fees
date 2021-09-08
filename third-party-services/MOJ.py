class MOJAPI:

    def __init__(self):
        pass

    def getOwnerData(self, land_number, block_number):
        self.land_number = land_number
        self.block_number = block_number

        if land_number=="1996" and block_number=="2021":
            return {"land_number":"1996", "block_number": "2021", "instrument_number": "5556667778", "identity_number": "1234567890", "first_name": "Lama", "last_name": "Alosaimi", "mobile": "0557864028", "email": "tutorialsemail511@gmail.com", "purchased_fee": "1500000", "land_space": 800}
        return None

    def getOwnerMeters(self, identity_number, city):
        if identity_number == "1234567890" and city == "Riyadh":
            return {"spaces": 7000}
        return {"spaces":3000}
        
    def health(self):
        return "OK!"