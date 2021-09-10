import mysql.connector


class mysqldb:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            port="33066",
            database="LandFees"
        )

        self.mycursor = self.mydb.cursor()

    def add(self, identity_number, instrument_number):
        sql = "INSERT INTO KAFKA_NOTIFIED_USERS (identity_number, instrument_number) VALUES (%s, %s)"
        val = (identity_number, instrument_number)
        self.mycursor.execute(sql, val)

        self.mydb.commit()

        print(self.mycursor.rowcount, "record inserted.")

    def isExists(self, identity_number, instrument_number):
        sql = "SELECT count(*)  FROM KAFKA_NOTIFIED_USERS WHERE identity_number=%s AND instrument_number=%s"
        val = (identity_number, instrument_number)
        self.mycursor.execute(sql, val)

        myresult = self.mycursor.fetchone()
        return myresult[0]
