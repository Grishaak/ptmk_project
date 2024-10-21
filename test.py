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

dbname = 'employee_db'
tablename = 'employee'

cursor = connection.cursor()
cursor.execute(sql.SQL(
    "DROP DATABASE IF EXISTS {}"
).format(sql.Identifier(dbname)))
cursor.execute(sql.SQL(
    "CREATE DATABASE {}"
).format(sql.Identifier(dbname)))

cursor.execute(sql.SQL(
    "GRANT ALL PRIVILEGES ON DATABASE {} TO {}"
).format(sql.Identifier(dbname),
         sql.Identifier('maguro')))

cursor.execute(sql.SQL(
    "CREATE TABLE IF NOT EXISTS {} "
).format(sql.Identifier()))

cursor.close()
connection.close()
