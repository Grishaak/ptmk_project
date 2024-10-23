import psycopg2
from psycopg2 import extensions

# Класс для представления подключения к базе данных.

class Connection:
    def __init__(self, database):
        self.database = database
        self.connection = psycopg2.connect(database=self.database.dbname, user=self.database.user,
                                           password=self.database.password)
        self.cursor = self.connection.cursor()

    def set_valid_connection(self):
        try:
            self.connection.set_client_encoding('utf8')

            autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
            self.connection.set_isolation_level(autocommit)
        except Exception:
            raise Exception('Cannot set valid connection.')

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def get_connection(self):
        self.set_valid_connection()
        return self.connection, self.cursor

    def get_conn(self):
        return self.connection
