import psycopg2
from psycopg2 import errors

# Класс для представления Database в виде набора параметров для подключения к ней.

class Database:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
