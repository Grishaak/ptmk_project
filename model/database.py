import psycopg2
from psycopg2 import errors


class Database:
    def __init__(self, db_name, host="127.0.0.1", password=None):
        self.connection = None
        self.cursor = None
        self.dbname = 'maguro_review'
        self.host = host

    def connect(self):
        try:
            self.connection = psycopg2.connect(dbname=self.dbname, user='postgres', password=self.password,
                                               host=self.host)
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(f"Error connecting to database: {e}")
            self.close()

        print(f"Connected to {self.dbname} on {self.host}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print(f"Closed connection to {self.dbname} on {self.host}")

    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id SERIAL PRIMARY KEY,
                    firstname VARCHAR(50) NOT NULL,
                    middlename VARCHAR(50),
                    lastname VARCHAR(50) NOT NULL,
                    birthdate DATE NOT NULL,
                    sex VARCHAR(10) NOT NULL
                )
            """)
            self.connection.commit()
            print("Employees table created successfully.")
        except errors.DatabaseError as e:
            print(f"Error creating employees table: {e}")
