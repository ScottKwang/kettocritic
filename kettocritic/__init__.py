from peewee import OperationalError
from playhouse.sqlite_ext import SqliteExtDatabase


DATABASE = 'my_database.db'
db = SqliteExtDatabase(DATABASE)


from kettocritic import models

db.connect()
try:
    print('Creating database tables')
    db.create_tables([
        models.Game,
        models.Tag,
        models.GameToTag,
        models.Team,
        models.Reviewer,
        models.Score,
        models.Review,
        models.ReviewerToTag,
    ])
    print('Database tables created')
except OperationalError:
    print('Database tables already exist')
