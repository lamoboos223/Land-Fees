class FasehAPI:

    def __init__(self):
        pass

    def isValid(self, instrument_number):
        if instrument_number == "5556667778":
            return True
        return False

    def issuedAt(self, instrument_number):
        if instrument_number == "5556667778":
            return 2020
        return 2021
