from playhouse.sqlite_ext import SqliteExtDatabase

DATABASE = 'my_database.db'
db = SqliteExtDatabase(DATABASE)

from kettocritic.router import Router
router = Router()
