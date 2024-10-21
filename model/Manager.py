from psycopg2 import extensions, sql, errors
from Database import Database
from Employee import Employee
from parameters import db_name, port, password, user, host


class Manager:
    TABLE_NAME = 'employees'

    def __init__(self):
        self.database = Database(db_name, host, user, password, port)
        self.connection, self.cursor = self.database.connection()

    def __str__(self):
        return f'Manager: {self.database}'

    # @staticmethod
    def create_connect_database(self):
        try:
            self.connection.set_client_encoding('utf8')

            autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
            self.connection.set_isolation_level(autocommit)
        except Exception:
            raise Exception('Cannot create and connect to database.')

    def create_table(self):
        try:
            self.cursor.execute(sql.SQL("""
                 CREATE TABLE IF NOT EXISTS {} (
                     id SERIAL PRIMARY KEY,
                     firstname VARCHAR(50) NOT NULL,
                     middlename VARCHAR(50),
                     lastname VARCHAR(50) NOT NULL,
                     birthdate DATE NOT NULL,
                     sex VARCHAR(10) NOT NULL
                 )
             """).format(sql.Identifier(self.TABLE_NAME)))
        except errors.DatabaseError as e:
            print(f"Error creating employees table: {e.cursor}")

    def insert_employee(self, *args, **kwargs):
        try:
            employee = Employee(*args, **kwargs)
            self.cursor.execute(sql.SQL("""
                 INSERT INTO {} (firstname, middlename, lastname, birthdate, sex)
                 VALUES (%s, %s, %s, %s, %s)
             """).format(sql.Identifier(self.TABLE_NAME)), employee.get_values())
        except errors.DatabaseError as e:
            raise e
