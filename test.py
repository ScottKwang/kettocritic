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

    def test_get_teams_sorted(self):
        """
        `router.get_teams(sorts=['id'])` is returning a list of reviews with missing 'name' and 'website' fields.
        Update the endpoint so that it correctly includes the 'name' and 'website' fields.
        """
        self.assertEqual(router.get_teams(sorts=['id']), [
            {'id': 1, 'name': 'IGN', 'website': 'https://www.ign.com/', 'num_reviews': 6, 'num_reviewers': 3},
            {'id': 2, 'name': 'metacritic', 'website': 'http://www.metacritic.com', 'num_reviews': 6, 'num_reviewers': 4},
            {'id': 3, 'name': 'PCGamer','website': 'http://www.pcgamer.com', 'num_reviews': 6, 'num_reviewers': 3}
        ])

    def test_get_reviews_with_normalized_scores(self):
        """
        Reviews can score games based on three different score types:

        `SCORE_TYPE_LETTER` 0-5
        `SCORE_TYPE_PERCENTAGE` 0-100
        `SCORE_TYPE_STARS` 0-5

        `router.get_reviews(sorts=['id'])` currently returns this raw score value.

        Instead, we want to compare scores across different `score_type`s by normalizing the `score`s to something more
        easily comparable. Add a `normalized_score` field that returns a score value from 0-100 and remove the raw `score` field.

        `SCORE_TYPE_LETTER` and `SCORE_TYPE_STARS` should multiply the raw score by 20 to produce the normalized score.
        """
        self.assertEqual(router.get_reviews(sorts=['id']), [
            {'game': 1, 'id': 1, 'reviewer': 1, 'normalized_score': 100, 'created_on': '2017-10-29 21:15:16.529267', 'title': "John Wall's Review of Assassins Creed Origins"},
            {'game': 1, 'id': 2, 'reviewer': 4, 'normalized_score': 91, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Stephen Curry's Review of Assassins Creed Origins"},
            {'game': 1, 'id': 3, 'reviewer': 8, 'normalized_score': 80, 'created_on': '2017-10-29 21:15:16.529267', 'title': "LeBron James's Review of Assassins Creed Origins"},
            {'game': 2, 'id': 4, 'reviewer': 2, 'normalized_score': 60, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Bradley Beal's Review of Cities Skylines"},
            {'game': 2, 'id': 5, 'reviewer': 5, 'normalized_score': 68, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Kevin Durant's Review of Cities Skylines"},
            {'game': 2, 'id': 6, 'reviewer': 9, 'normalized_score': 80, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Derrick Rose's Review of Cities Skylines"},
            {'game': 3, 'id': 7, 'reviewer': 3, 'normalized_score': 80, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Mike Scott's Review of Cuphead"},
            {'game': 3, 'id': 8, 'reviewer': 6, 'normalized_score': 85, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Klay Thompson's Review of Cuphead"},
            {'game': 3, 'id': 9, 'reviewer': 10, 'normalized_score': 60, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Dwyane Wade's Review of Cuphead"},
            {'game': 4, 'id': 10, 'reviewer': 1, 'normalized_score': 60, 'created_on': '2017-10-29 21:15:16.529267', 'title': "John Wall's Review of Destiny 2"},
            {'game': 4, 'id': 11, 'reviewer': 7, 'normalized_score': 61, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Draymond Green's Review of Destiny 2"},
            {'game': 4, 'id': 12, 'reviewer': 8, 'normalized_score': 40, 'created_on': '2017-10-29 21:15:16.529267', 'title': "LeBron James's Review of Destiny 2"},
            {'game': 5, 'id': 13, 'reviewer': 2, 'normalized_score': 100, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Bradley Beal's Review of Super Smash Bros. for Wii U"},
            {'game': 5, 'id': 14, 'reviewer': 4, 'normalized_score': 97, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Stephen Curry's Review of Super Smash Bros. for Wii U"},
            {'game': 5, 'id': 15, 'reviewer': 9, 'normalized_score': 100, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Derrick Rose's Review of Super Smash Bros. for Wii U"},
            {'game': 6, 'id': 16, 'reviewer': 3, 'normalized_score': 80, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Mike Scott's Review of Super Meat Boy"},
            {'game': 5, 'id': 17, 'reviewer': 5, 'normalized_score': 88, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Kevin Durant's Review of Super Smash Bros. for Wii U"},
            {'game': 5, 'id': 18, 'reviewer': 10, 'normalized_score': 80, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Dwyane Wade's Review of Super Smash Bros. for Wii U"}
        ])

    def test_get_games_with_average_scores(self):
        """
        `router.get_games(sorts=['id'])` currently does not include the average score. We would like to be able to calculate and
        present the average score for each game.
        """
        self.assertEqual(router.get_games(sorts=['id']), [
            {'id': 1, 'name': 'Assassins Creed Origins', 'average_score': 90.33333333333333},
            {'id': 2, 'name': 'Cities Skylines', 'average_score': 69.33333333333333},
            {'id': 3, 'name': 'Cuphead', 'average_score': 75.0},
            {'id': 4, 'name': 'Destiny 2', 'average_score': 53.666666666666664},
            {'id': 5, 'name': 'Super Smash Bros. for Wii U', 'average_score': 93.0},
            {'id': 6, 'name': 'Super Meat Boy', 'average_score': 80.0}
        ])

    def test_get_games_with_average_score_filter(self):
        """
        `router.get_games(filter={'average_score__gt': 70})` isn't correctly filtering the list of games
        to only include games with an average score of 70 or greater.
        Update the filtering to correctly filter the list of games by average score.
        """
        self.assertEqual(router.get_games(filters={'average_score__gte': 70}), [
            {'id': 1, 'average_score': 90.33333333333333, 'name': 'Assassins Creed Origins'},
            {'id': 3, 'average_score': 75.0, 'name': 'Cuphead'},
            {'id': 5, 'average_score': 93.0, 'name': 'Super Smash Bros. for Wii U'},
            {'id': 6, 'average_score': 80.0, 'name': 'Super Meat Boy'}
        ])

    def test_get_reviews_sorted_by_reviewer_team_name(self):
        """
        `router.get_reviews(sorts=['reviewer__team__name', 'id'])` isn't correctly sorting the list of reviews by reviewer team name.
        Modify the `ModelView` class such that queries can be sorted by related properties.

        Note: reviewers 1-3 are on team "IGN", reviewers 4-7 are on team "metacritic", and reviewers 8-10 are on team "PCGamer"
        """
        self.assertEqual(router.get_reviews(sorts=['reviewer__team__name', 'id']), [
            {'reviewer': 1, 'id': 1, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 100, 'game': 1, 'title': "John Wall's Review of Assassins Creed Origins"},
            {'reviewer': 2, 'id': 4, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 60, 'game': 2, 'title': "Bradley Beal's Review of Cities Skylines"},
            {'reviewer': 3, 'id': 7, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 80, 'game': 3, 'title': "Mike Scott's Review of Cuphead"},
            {'reviewer': 1, 'id': 10, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 60, 'game': 4, 'title': "John Wall's Review of Destiny 2"},
            {'reviewer': 2, 'id': 13, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 100, 'game': 5, 'title': "Bradley Beal's Review of Super Smash Bros. for Wii U"},
            {'reviewer': 3, 'id': 16, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 80, 'game': 6, 'title': "Mike Scott's Review of Super Meat Boy"},
            {'reviewer': 4, 'id': 2, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 91, 'game': 1, 'title': "Stephen Curry's Review of Assassins Creed Origins"},
            {'reviewer': 5, 'id': 5, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 68, 'game': 2, 'title': "Kevin Durant's Review of Cities Skylines"},
            {'reviewer': 6, 'id': 8, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 85, 'game': 3, 'title': "Klay Thompson's Review of Cuphead"},
            {'reviewer': 7, 'id': 11, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 61, 'game': 4, 'title': "Draymond Green's Review of Destiny 2"},
            {'reviewer': 4, 'id': 14, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 97, 'game': 5, 'title': "Stephen Curry's Review of Super Smash Bros. for Wii U"},
            {'reviewer': 5, 'id': 17, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 88, 'game': 5, 'title': "Kevin Durant's Review of Super Smash Bros. for Wii U"},
            {'reviewer': 8, 'id': 3, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 80, 'game': 1, 'title': "LeBron James's Review of Assassins Creed Origins"},
            {'reviewer': 9, 'id': 6, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 80, 'game': 2, 'title': "Derrick Rose's Review of Cities Skylines"},
            {'reviewer': 10, 'id': 9, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 60, 'game': 3, 'title': "Dwyane Wade's Review of Cuphead"},
            {'reviewer': 8, 'id': 12, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 40, 'game': 4, 'title': "LeBron James's Review of Destiny 2"},
            {'reviewer': 9, 'id': 15, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 100, 'game': 5, 'title': "Derrick Rose's Review of Super Smash Bros. for Wii U"},
            {'reviewer': 10, 'id': 18, 'created_on': '2017-10-29 21:15:16.529267', 'normalized_score': 80, 'game': 5, 'title': "Dwyane Wade's Review of Super Smash Bros. for Wii U"}
        ])


if __name__ == '__main__':
    from subprocess import call
    call(["rm", "my_database.db"])
    unittest.main()
