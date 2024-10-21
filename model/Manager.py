from Database import Database
from Employee import Employee


class Manager:
    @staticmethod
    def create_connect_database(db_name, host, user, password, port):
        database = Database(db_name, host, user, password, port)
