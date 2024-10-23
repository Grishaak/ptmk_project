import random
import time
import multiprocessing
from psycopg2 import extensions, sql, errors
from model.Database import Database
from model.Employee import Employee
from model.parameters import db_name, port, password, user, host
from model.Connection import Connection


# Класс Manager для курирования основными методами и сущностями в model.
# Классы Database, Connection, Employee нужны для более четкого преставления вида параметров.

class Manager:
    TABLE_NAME = 'employees'

    def __init__(self):
        self.database = Database(db_name, user, password, host, port)
        self.table_created = self.__check__()

    def __str__(self):
        return f'Manager: {self.database}'

    def __check__(self):
        explorer = Connection(self.database)
        connection, cursor = explorer.get_connection()
        cursor.execute(
            sql.SQL("""SELECT to_regclass({}) is not null as new_table""").format(sql.Literal(self.TABLE_NAME)))
        data = cursor.fetchone()
        explorer.close_connection()

        if data[0] == False:
            print("Table has not been created")
            return False
        print("Table has been created")
        return True

    def is_created_table(self):
        if self.table_created:
            return True
        print("Table is not existed")
        return False

    def is_created_table_exception(self):
        if not self.table_created:
            raise Exception

    def create_table(self):
        try:
            explorer = Connection(self.database)
            connection, cursor = explorer.get_connection()
            cursor.execute(sql.SQL("""
                                 DROP TABLE IF EXISTS {};
                                """).format(sql.Identifier(self.TABLE_NAME)))
            cursor.execute(sql.SQL("""
                     CREATE TABLE IF NOT EXISTS {} (
                         id SERIAL PRIMARY KEY,
                         firstname VARCHAR(50) NOT NULL,
                         middle_name VARCHAR(50),
                         lastname VARCHAR(50) NOT NULL,
                         birthdate DATE NOT NULL,
                         sex VARCHAR(10) NOT NULL
                     )
                 """).format(sql.Identifier(self.TABLE_NAME)),
                           sql.Identifier(self.TABLE_NAME))
            print(f"{self.TABLE_NAME} Created")
            explorer.close_connection()
            self.table_created = True
        except errors.UndefinedTable:
            print("Table is not existed")

    def drop_table(self):
        explorer = Connection(self.database)
        connection, cursor = explorer.get_connection()
        cursor.execute(sql.SQL(""" DROP TABLE IF EXISTS {};""").format(sql.Identifier(self.TABLE_NAME)))
        explorer.close_connection()
        self.table_created = False

    def insert_employee(self, *args, **kwargs):
        try:
            explorer = Connection(self.database)
            connection, cursor = explorer.get_connection()
            employee = Employee(*args, **kwargs)
            cursor.execute(sql.SQL("""
                     INSERT INTO {} (firstname, middle_name, lastname, birthdate, sex)
                     VALUES ({})
                 """).format(sql.Identifier(self.TABLE_NAME),
                             sql.SQL(', ').join(map(sql.Literal, employee.get_values()))
                             )
                           )
            explorer.close_connection()
        except (errors.UndefinedTable, Exception):
            print("Table is not existed")

    def show_all_employees(self):
        try:
            # self.is_created_table()
            explorer = Connection(self.database)
            connection, cursor = explorer.get_connection()
            cursor.execute(sql.SQL("""
                    SELECT *,ROUND((current_date - birthdate) / 365.25) AS ages FROM {}
                 """).format(sql.Identifier(self.TABLE_NAME)))
            rows = cursor.fetchall()
            for row in rows:
                print(*row)
            explorer.close_connection()
        except (errors.UndefinedTable, Exception):
            print("Table is not existed")

    def process_worker(self, employees):
        explorer = Connection(self.database)
        connection, cursor = explorer.get_connection()
        args = ','.join(str(cursor.mogrify("(%s,%s,%s,%s,%s)", x).decode('utf8')) for x in employees)
        query = f"INSERT INTO {self.TABLE_NAME} (firstname, middle_name, lastname, birthdate, sex) VALUES " + (
            args)
        cursor.execute(query)
        explorer.close_connection()

    def execute_large_request(self):
        try:
            self.is_created_table_exception()
            chars = [i for i in 'abcdeghijklmnopqrstuvwxyz']
            days = [str(i) for i in range(1, 28)]
            month = [str(i) for i in range(1, 12)]
            years = [str(i) for i in range(1970, 2005)]
            rand_names = ["".join(random.choice(chars) for j in range(random.randint(3, 14))) for i in range(500)]
            sex = ('male', 'female')
            f_names = ["f" + random.choice(rand_names) for i in range(100)]
            dates = ['-'.join([random.choice(years), random.choice(month), random.choice(days)]) for i in range(500)]
            query_volume = 100000
            processes = 10
            start = 0
            end = start + query_volume
            x1 = time.time()
            employees = []
            while end <= (query_volume * processes):
                min_quyery = []
                for j in range(query_volume - 1):
                    min_quyery.append([random.choice(rand_names),
                                       random.choice(rand_names),
                                       random.choice(rand_names),
                                       random.choice(dates),
                                       random.choice(sex)
                                       ])
                    if j % 10000 == 0:
                        min_quyery.append([random.choice(rand_names),
                                           random.choice(f_names),
                                           random.choice(rand_names),
                                           random.choice(dates),
                                           'male'
                                           ])
                employees.append(min_quyery)
                start, end = end, end + query_volume
            with multiprocessing.Pool(processes=10) as pool:
                pool.map(self.process_worker, employees)

            x2 = time.time()
            x3 = abs(x1 - x2)
            print(f"Время потрачено: {x3:.3f} s")

        # except errors.UndefinedTable:
        #     prin
        except Exception:
            print("Table is not existed")

    def shower_worker(self):
        try:
            explorer = Connection(self.database)
            connection, cursor = explorer.get_connection()
            query = sql.SQL("""SELECT id, sex,middle_name FROM {}
                    WHERE middle_name LIKE 'f%' AND sex = 'male'
                    """).format(sql.Identifier(self.TABLE_NAME))
            cursor.execute(query)
            data = cursor.fetchall()
            for d in data:
                print(d)
        except Exception as e:
            raise e
        else:
            explorer.close_connection()

    def show_all_employees_for_large_request_not_optimal(self):
        try:
            x1 = time.time()
            with multiprocessing.Pool(processes=8):
                self.shower_worker()
            x2 = time.time()
            x3 = x2 - x1
            print(f"Время: {x3 * 1000:.4f} ms")

        except (errors.UndefinedTable):
            print("Table is not existed")

    def show_all_employees_for_large_request_optimal(self):
        try:
            explorer = Connection(self.database)
            connection, cursor = explorer.get_connection()
            x1 = time.time()
            query = sql.SQL("""SELECT id, sex,middle_name FROM {}
                            WHERE middle_name LIKE 'f%' AND sex = 'male'
                            """).format(sql.Identifier(self.TABLE_NAME))
            cursor.execute(query)
            data = cursor.fetchall()
            x2 = time.time()
            for d in data:
                print(d)
            explorer.close_connection()
            x3 = x2 - x1
            print(f"Время: {x3 * 1000:.3f} ms")
        except (errors.UndefinedTable, Exception):
            print("Table is not existed")
