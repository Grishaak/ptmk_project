import psycopg2
from psycopg2 import errors


class Database:
    def __init__(self, dbname, host, user, password, port):
        self.connection = None
        self.cursor = None
        self.dbname = dbname
        self.host = host
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        try:
            self.connection = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password,
                                               host=self.host, port=self.port)
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(f"Error connecting to database: {e}")
            self.close()
        else:
            return self.connection, self.cursor

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
