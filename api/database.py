import os

import mysql.connector
from dotenv import load_dotenv


load_dotenv()


class Database:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password=os.getenv("MYSQL_PASSWORD"),
                database="sales"
            )

            self.cursor = self.connection.cursor()

            return True

        except mysql.connector.Error as error:
            print("Connection error:", error)
            return False

    def close(self):
        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()