import datetime
from kettocritic import db
from peewee import *


class BaseModel(Model):

    def __str__(self):
        return str(self.id)

    class Meta:
        database = db


class Game(BaseModel):
    name = CharField(unique=True)


class Tag(BaseModel):
    name = CharField(unique=True)


class GameToTag(BaseModel):
    game = ForeignKeyField(Game)
    tag = ForeignKeyField(Tag)

    class Meta:
        primary_key = CompositeKey('game', 'tag')


class Team(BaseModel):
    name = CharField(unique=True)
    website = CharField(unique=True)


class Reviewer(BaseModel):
    name = CharField(unique=True)
    team = ForeignKeyField(Team)


class Score(BaseModel):
    SCORE_TYPE_LETTER = 10
    SCORE_TYPE_PERCENTAGE = 20
    SCORE_TYPE_STARS = 30
    SCORE_TYPE_CHOICES = (
        (SCORE_TYPE_LETTER, 'Letter'),
        (SCORE_TYPE_PERCENTAGE, 'Percentage'),
        (SCORE_TYPE_STARS, 'Stars'),
    )
    score = IntegerField() 
    score_type = IntegerField(choices=SCORE_TYPE_CHOICES)


class Review(BaseModel):
    created_on = DateTimeField(default=datetime.datetime.now)
    description = TextField()
    game = ForeignKeyField(Game)
    reviewer = ForeignKeyField(Reviewer)
    score = ForeignKeyField(Score)
    title = CharField()


class ReviewerToTag(BaseModel):
    reviewer = ForeignKeyField(Reviewer)
    tag = ForeignKeyField(Tag)

    class Meta:
        primary_key = CompositeKey('reviewer', 'tag')
