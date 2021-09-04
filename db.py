import mysql.connector

class mysqldb:

    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="sa",
        password="sa",
        database="LandFees"
        )

        self.mycursor = self.mydb.cursor()

    def add(self, identity_number, instrument_number):
        sql = "INSERT INTO NotifiedUsers (identity_number, instrument_number) VALUES (%s, %s)"
        val = (identity_number, instrument_number)
        self.mycursor.execute(sql, val)

        self.mydb.commit()

        print(self.mycursor.rowcount, "record inserted.")

    
    def isExists(self, identity_number, instrument_number):
        sql = "SELECT count(*)  FROM NotifiedUsers WHERE 'identity_number'=%s AND 'instrument_number'=%s"
        val = (identity_number, instrument_number)
        self.mycursor.execute(sql, val)

        myresult = self.mycursor.fetchall()

        for x in myresult:
            print(x)
            return x