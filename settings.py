import peewee
from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'orm_py25',
    user = 'zhokee',
    password = '1',
    host = 'localhost',
    port = 5432
)
