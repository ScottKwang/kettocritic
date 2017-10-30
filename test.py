import unittest
from kettocritic import router
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

    def test_reviewer_view_get(self):
        """
        `router.get_reviews()` is returning a list of reviews with missing 'create_on' and 'description' fields.
        Fix the `query` function so it correctly includes the 'date' and 'description' fields.
        """
        pass

    def test_review_view_get_with_filter(self):
        """
        `Review.get(filter='average_score_gte=70')` isn't correctly filtering the list of reviews to only
        include reviews with an average score below 70.
        Fix the `query` function so it correctly filters the list of reivews by average score.
        """
        pass

    def test_game_view_get_with_sort(self):
        """
        `GameView.get(sort='team__name')` isn't correctly sorting the list of games by team name.
        Modify the `ModelView` class such that queries can be sorted by related properties.
        """
        pass


if __name__ == '__main__':
    unittest.main()
