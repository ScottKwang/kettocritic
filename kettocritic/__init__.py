from peewee import OperationalError
from playhouse.sqlite_ext import SqliteExtDatabase

DATABASE = 'my_database.db'
db = SqliteExtDatabase(DATABASE)
