# import psycopg2
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
    "DROP TABLE IF EXISTS {}.{}"
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

cursor.execute(sql.SQL(
    "DROP TABLE IF EXISTS {} "
).format(sql.Identifier(table_name)))

cursor.close()
connection.close()
