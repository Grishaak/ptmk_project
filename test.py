# import psycopg2
import random

from psycopg2 import extensions, connect, sql

connection = connect(database="maguro_review",
                     user="maguro",
                     password="vbifyz228422",
                     host="127.0.0.1",
                     port="5432")

connection.set_client_encoding('utf8')

autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
connection.set_isolation_level(autocommit)

dbname = 'maguro_review'
table_name = 'employee'

cursor = connection.cursor()

cursor.execute(sql.SQL(
    "GRANT ALL PRIVILEGES ON DATABASE {} TO {}"
).format(sql.Identifier(dbname),
         sql.Identifier('maguro')))

cursor.execute(sql.SQL(
    "DROP TABLE IF EXISTS {}"
).format(sql.Identifier(dbname),
         sql.Identifier(table_name)))

cursor.execute(sql.SQL(
    """
    CREATE TABLE IF NOT EXISTS {} (
        id SERIAL PRIMARY KEY,
        firstname VARCHAR(50) NOT NULL,
        middle_name VARCHAR(50),
        lastname VARCHAR(50) NOT NULL,
        birthdate DATE NOT NULL,
        sex VARCHAR(10) NOT NULL)""").format(
    sql.Identifier(table_name)))

first_name = "Alex"
middle_name = "Sanchos"
last_name = "Vargos"
birthdate = "2000-06-30"
sex = "male"

values = first_name, middle_name, last_name, birthdate, sex

query = sql.SQL(
    "INSERT INTO {} (firstname, middle_name, lastname, birthdate, sex) VALUES ({}, {}, {}, {}, {}) ;"
).format(sql.Identifier(table_name),
         sql.Literal(first_name),
         sql.Literal(middle_name),
         sql.Literal(last_name),
         sql.Literal(birthdate),
         sql.Literal(sex),
         )

cursor.execute(query)

cursor.execute(sql.SQL(
    """SELECT firstname AS Age FROM {}"""
).format(sql.Identifier(table_name)))

data = cursor.fetchall()
for row in data:
    print(row)
#
chars = [i for i in 'abcdefghijklmnopqrstuvwxyzABCDEF1234567890']
days = [str(i) for i in range(1, 28)]
month = [str(i) for i in range(1, 12)]
years = [str(i) for i in range(1970, 2005)]
rand_names = ["".join(random.choice(chars) for j in range(random.randint(3, 14))) for i in range(500)]
sex = ('male', 'female')

dates = ['-'.join([random.choice(years), random.choice(month), random.choice(days)]) for i in range(500)]

employees = []
for i in range(10000):
    employees.append([random.choice(rand_names),
                      random.choice(rand_names),
                      random.choice(rand_names),
                      random.choice(dates),
                      random.choice(sex)
                      ])
args = ','.join(str(cursor.mogrify("(%s,%s,%s,%s,%s)", x).decode('utf8')) for x in employees)
# print(args)
# query = sql.SQL(
#     'INSERT INTO {} (firstname, middle_name, lastname, birthdate, sex) VALUES {};'
#     .format(sql.Identifier(table_name),
#             sql.SQL(args)))

query = "INSERT INTO employee (firstname, middle_name, lastname, birthdate, sex) VALUES " + (args)
cursor.execute(query)

cursor.execute(sql.SQL(
    """SELECT firstname AS Age FROM {}"""
).format(sql.Identifier(table_name)))

data = cursor.fetchall()
for row in data:
    print(row)


# print(query)
# print(employees.__sizeof__() // 1024)
cursor.execute(sql.SQL(
    "DROP TABLE IF EXISTS {} "
).format(sql.Identifier(table_name)))

cursor.close()
connection.close()
