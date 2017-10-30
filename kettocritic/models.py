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

    @property
    def average_score(self):
        reviews = self.reviews
        if not reviews:
            return 0
        total_score = sum(review.score.normalized_score for review in reviews)
        return total_score / len(reviews)


class Tag(BaseModel):
    name = CharField(unique=True)


class GameToTag(BaseModel):
    game = ForeignKeyField(Game, related_name='game_to_tags')
    tag = ForeignKeyField(Tag, related_name='tag_to_games')

    class Meta:
        primary_key = CompositeKey('game', 'tag')


class Team(BaseModel):
    name = CharField(unique=True)
    website = CharField(unique=True)


class Reviewer(BaseModel):
    name = CharField(unique=True)
    team = ForeignKeyField(Team, related_name='reviewers')


class Score(BaseModel):
    SCORE_TYPE_LETTER = 10  # 1 - 5
    SCORE_TYPE_PERCENTAGE = 20  # 0 - 100
    SCORE_TYPE_STARS = 30  # 0 - 5
    SCORE_TYPE_CHOICES = (
        (SCORE_TYPE_LETTER, 'Letter'),
        (SCORE_TYPE_PERCENTAGE, 'Percentage'),
        (SCORE_TYPE_STARS, 'Stars'),
    )
    score = IntegerField()
    score_type = IntegerField(choices=SCORE_TYPE_CHOICES)

    @property
    def normalized_score(self):
        if self.score_type == self.SCORE_TYPE_LETTER or \
                self.score_type == self.SCORE_TYPE_STARS:
            return self.score * 20  # potential refactor into computed from constant range
        return self.score


class Review(BaseModel):
    created_on = DateTimeField(default=datetime.datetime.strptime('2017-10-29 21:15:16.529267', '%Y-%m-%d %H:%M:%S.%f'))
    description = TextField()
    game = ForeignKeyField(Game, related_name='reviews')
    reviewer = ForeignKeyField(Reviewer, related_name='reviews')
    score = ForeignKeyField(Score, related_name='review')
    title = CharField()


class ReviewerToTag(BaseModel):
    reviewer = ForeignKeyField(Reviewer, related_name='reviewer_to_tags')
    tag = ForeignKeyField(Tag, related_name='tag_to_reviewers')

    class Meta:
        primary_key = CompositeKey('reviewer', 'tag')
