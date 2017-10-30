import unittest
from peewee import IntegrityError

from db_utils import create_tables, create_data, drop_tables


class FailingTests(unittest.TestCase):

    def setUp(self):
        """
        Set up fixtures.
        """
        create_tables()
        create_data()

    def tearDown(self):
        """
        Tear down Fixtures.
        """
        drop_tables()

    """
    def _create_object(self, model, **kwargs):
        try:
            with self.database.transaction():
                object = model.create(**kwargs)
        except IntegrityError:
            object = model.get(**kwargs)
        self.objects_to_destroy.append(object)
        return object

    def _create_game(self, name):
        create_kwargs = {
            'name': name,
        }
        return self._create_object(models.Game, **create_kwargs)

    def _create_team(self, name, website):
        create_kwargs = {
            'name': name,
            'website': website,
        }
        return self._create_object(models.Team, **create_kwargs)

    def _create_reviewer(self, name, team):
        create_kwargs = {
            'name': name,
            'team': team,
        }
        return self._create_object(models.Reviewer, **create_kwargs)

    def _create_review(self, game, reviewer, score_type, score_value):
        create_kwargs = {
            'game': game,
            'reviewer': reviewer,
            'title': "{}'s Review of {}".format(reviewer.name, game.name),
            'description': "{} gives his take on {}".format(reviewer.name, game.name),
            'score': self._create_score(score_type, score_value),
        }
        return self._create_object(models.Review, **create_kwargs)

    def _create_score(self, score_type, score_value):
        create_kwargs = {
            'score': score_value,
            'score_type': score_type,
        }
        return self._create_object(models.Score, **create_kwargs)
    """

    def test_reviewer_view_get(self):
        """
        `ReviewersView.get()` is returning a list of reviews with missing 'date' and 'description' fields.
        Fix the `get` function so it correctly includes the 'date' and 'description' fields.
        """
        pass

    def test_game_view_get_with_sort(self):
        """
        `GameView.get(sort='team')` isn't correctly sorting the list of games by team name.
        Fix the `get` function so it correctly sorts the list of games by related team name.
        """
        pass

    def test_review_view_get_with_filter(self):
        """
        `Review.get(filter='average_score_gte=70')` isn't correctly filtering the list of reviews to only
        include reviews with an average score below 70.
        Fix the `get` function so it correctly filters the list of reivews by average score.
        """
        pass


if __name__ == '__main__':
    unittest.main()
