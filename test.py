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

    def test_team_view_get(self):
        """
        `router.get_teams(sorts=['id'])` is returning a list of reviews with missing 'name' and 'website' fields.
        Update the endpoint so that it correctly includes the 'name' and 'website' fields.
        """
        self.assertEqual(router.get_teams(sorts=['id']), [
            {'num_reviews': 6, 'id': 1, 'name': 'IGN', 'num_reviewers': 3, 'website': 'https://www.ign.com/'},
            {'num_reviews': 6, 'id': 2, 'name': 'metacritic', 'num_reviewers': 4, 'website': 'http://www.metacritic.com'},
            {'num_reviews': 6, 'id': 3, 'name': 'PCGamer', 'num_reviewers': 3, 'website': 'http://www.pcgamer.com'}
        ])

    def test_review_view_get_with_normalized_score(self):
        """
        `router.get_reviews(sorts=['id'])` currently returns the raw score
        `SCORE_TYPE_LETTER` 0-5
        `SCORE_TYPE_PERCENTAGE` 0-100
        `SCORE_TYPE_STARS` 0-5
        We also want the ability to compare scores across different `score_type`s by normalizing the `score`s to something more
        easily comparable. (0-100)
        """
        self.assertEqual(router.get_reviews(sorts=['id']), [
            {'game': 1, 'score': 1, 'id': 1, 'description': 'John Wall Takes an in-depth look at Assassins Creed Origins', 'normalized_score': 100, 'reviewer': 1, 'created_on': '2017-10-29 21:15:16.529267', 'title': "John Wall's Review of Assassins Creed Origins"},
            {'game': 1, 'score': 2, 'id': 2, 'description': 'Stephen Curry Takes an in-depth look at Assassins Creed Origins', 'normalized_score': 91, 'reviewer': 4, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Stephen Curry's Review of Assassins Creed Origins"},
            {'game': 1, 'score': 3, 'id': 3, 'description': 'LeBron James Takes an in-depth look at Assassins Creed Origins', 'normalized_score': 80, 'reviewer': 8, 'created_on': '2017-10-29 21:15:16.529267', 'title': "LeBron James's Review of Assassins Creed Origins"},
            {'game': 2, 'score': 4, 'id': 4, 'description': 'Bradley Beal Takes an in-depth look at Cities Skylines', 'normalized_score': 60, 'reviewer': 2, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Bradley Beal's Review of Cities Skylines"},
            {'game': 2, 'score': 5, 'id': 5, 'description': 'Kevin Durant Takes an in-depth look at Cities Skylines', 'normalized_score': 68, 'reviewer': 5, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Kevin Durant's Review of Cities Skylines"},
            {'game': 2, 'score': 6, 'id': 6, 'description': 'Derrick Rose Takes an in-depth look at Cities Skylines', 'normalized_score': 80, 'reviewer': 9, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Derrick Rose's Review of Cities Skylines"},
            {'game': 3, 'score': 7, 'id': 7, 'description': 'Mike Scott Takes an in-depth look at Cuphead', 'normalized_score': 80, 'reviewer': 3, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Mike Scott's Review of Cuphead"},
            {'game': 3, 'score': 8, 'id': 8, 'description': 'Klay Thompson Takes an in-depth look at Cuphead', 'normalized_score': 85, 'reviewer': 6, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Klay Thompson's Review of Cuphead"},
            {'game': 3, 'score': 9, 'id': 9, 'description': 'Dwyane Wade Takes an in-depth look at Cuphead', 'normalized_score': 60, 'reviewer': 10, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Dwyane Wade's Review of Cuphead"},
            {'game': 4, 'score': 10, 'id': 10, 'description': 'John Wall Takes an in-depth look at Destiny 2', 'normalized_score': 60, 'reviewer': 1, 'created_on': '2017-10-29 21:15:16.529267', 'title': "John Wall's Review of Destiny 2"},
            {'game': 4, 'score': 11, 'id': 11, 'description': 'Draymond Green Takes an in-depth look at Destiny 2', 'normalized_score': 61, 'reviewer': 7, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Draymond Green's Review of Destiny 2"},
            {'game': 4, 'score': 12, 'id': 12, 'description': 'LeBron James Takes an in-depth look at Destiny 2', 'normalized_score': 40, 'reviewer': 8, 'created_on': '2017-10-29 21:15:16.529267', 'title': "LeBron James's Review of Destiny 2"},
            {'game': 5, 'score': 13, 'id': 13, 'description': 'Bradley Beal Takes an in-depth look at Super Smash Bros. for Wii U', 'normalized_score': 100, 'reviewer': 2, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Bradley Beal's Review of Super Smash Bros. for Wii U"},
            {'game': 5, 'score': 14, 'id': 14, 'description': 'Stephen Curry Takes an in-depth look at Super Smash Bros. for Wii U', 'normalized_score': 97, 'reviewer': 4, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Stephen Curry's Review of Super Smash Bros. for Wii U"},
            {'game': 5, 'score': 15, 'id': 15, 'description': 'Derrick Rose Takes an in-depth look at Super Smash Bros. for Wii U', 'normalized_score': 100, 'reviewer': 9, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Derrick Rose's Review of Super Smash Bros. for Wii U"},
            {'game': 6, 'score': 16, 'id': 16, 'description': 'Mike Scott Takes an in-depth look at Super Meat Boy', 'normalized_score': 80, 'reviewer': 3, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Mike Scott's Review of Super Meat Boy"},
            {'game': 5, 'score': 17, 'id': 17, 'description': 'Kevin Durant Takes an in-depth look at Super Smash Bros. for Wii U', 'normalized_score': 88, 'reviewer': 5, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Kevin Durant's Review of Super Smash Bros. for Wii U"},
            {'game': 5, 'score': 18, 'id': 18, 'description': 'Dwyane Wade Takes an in-depth look at Super Smash Bros. for Wii U', 'normalized_score': 80, 'reviewer': 10, 'created_on': '2017-10-29 21:15:16.529267', 'title': "Dwyane Wade's Review of Super Smash Bros. for Wii U"}
        ])

    def test_game_view_get_with_calculated_values(self):
        """
        `router.get_games(sorts=['id'])` currently does not include the average score. We would like to be able to calculate and
        present the average score for each game.
        """
        self.assertEqual(router.get_games(sorts=['id']), [
            {'name': 'Assassins Creed Origins', 'id': 1, 'average_score': 90.33333333333333},
            {'name': 'Cities Skylines', 'id': 2, 'average_score': 69.33333333333333},
            {'name': 'Cuphead', 'id': 3, 'average_score': 75.0},
            {'name': 'Destiny 2', 'id': 4, 'average_score': 53.666666666666664},
            {'name': 'Super Smash Bros. for Wii U', 'id': 5, 'average_score': 93.0},
            {'name': 'Super Meat Boy', 'id': 6, 'average_score': 80.0}
        ])

    def test_game_view_get_with_filter(self):
        """
        `router.get_games(filter={'average_score__gte': 70})` isn't correctly filtering the list of games
        to only include games with an average score of 70 or greater.
        Update the filtering to correctly filter the list of games by average score.
        Easy Mode: Implement filtering after the objects have been serialized
        Hard Mode: Implement filtering at the ORM level
        """
        self.assertEqual(router.get_games(filters={'average_score__gte': 70}), [
            {'average_score': 90.33333333333333, 'name': 'Assassins Creed Origins', 'id': 1},
            {'average_score': 75.0, 'name': 'Cuphead', 'id': 3},
            {'average_score': 93.0, 'name': 'Super Smash Bros. for Wii U', 'id': 5},
            {'average_score': 80.0, 'name': 'Super Meat Boy', 'id': 6}
        ])

    def test_review_view_get_with_sort(self):
        """
        `router.get_reviews(sorts=['reviewer__team__name', 'id'])` isn't correctly sorting the list of reviews by reviewer team name.
        Modify the `ModelView` class such that queries can be sorted by related properties.
        Extra Credit: expand related fields so that we are able to see the related teams in the router output
        Note: Test should not fail if you complete the extra credit
        """
        self.assertEqual(router.get_reviews(sorts=['reviewer__team__name', 'id']), [
            {'description': 'John Wall Takes an in-depth look at Assassins Creed Origins', 'reviewer': 1, 'created_on': '2017-10-29 21:15:16.529267', 'id': 1, 'normalized_score': 100, 'score': 1, 'game': 1, 'title': "John Wall's Review of Assassins Creed Origins"},
            {'description': 'Bradley Beal Takes an in-depth look at Cities Skylines', 'reviewer': 2, 'created_on': '2017-10-29 21:15:16.529267', 'id': 4, 'normalized_score': 60, 'score': 4, 'game': 2, 'title': "Bradley Beal's Review of Cities Skylines"},
            {'description': 'Mike Scott Takes an in-depth look at Cuphead', 'reviewer': 3, 'created_on': '2017-10-29 21:15:16.529267', 'id': 7, 'normalized_score': 80, 'score': 7, 'game': 3, 'title': "Mike Scott's Review of Cuphead"},
            {'description': 'John Wall Takes an in-depth look at Destiny 2', 'reviewer': 1, 'created_on': '2017-10-29 21:15:16.529267', 'id': 10, 'normalized_score': 60, 'score': 10, 'game': 4, 'title': "John Wall's Review of Destiny 2"},
            {'description': 'Bradley Beal Takes an in-depth look at Super Smash Bros. for Wii U', 'reviewer': 2, 'created_on': '2017-10-29 21:15:16.529267', 'id': 13, 'normalized_score': 100, 'score': 13, 'game': 5, 'title': "Bradley Beal's Review of Super Smash Bros. for Wii U"},
            {'description': 'Mike Scott Takes an in-depth look at Super Meat Boy', 'reviewer': 3, 'created_on': '2017-10-29 21:15:16.529267', 'id': 16, 'normalized_score': 80, 'score': 16, 'game': 6, 'title': "Mike Scott's Review of Super Meat Boy"},
            {'description': 'Stephen Curry Takes an in-depth look at Assassins Creed Origins', 'reviewer': 4, 'created_on': '2017-10-29 21:15:16.529267', 'id': 2, 'normalized_score': 91, 'score': 2, 'game': 1, 'title': "Stephen Curry's Review of Assassins Creed Origins"},
            {'description': 'Kevin Durant Takes an in-depth look at Cities Skylines', 'reviewer': 5, 'created_on': '2017-10-29 21:15:16.529267', 'id': 5, 'normalized_score': 68, 'score': 5, 'game': 2, 'title': "Kevin Durant's Review of Cities Skylines"},
            {'description': 'Klay Thompson Takes an in-depth look at Cuphead', 'reviewer': 6, 'created_on': '2017-10-29 21:15:16.529267', 'id': 8, 'normalized_score': 85, 'score': 8, 'game': 3, 'title': "Klay Thompson's Review of Cuphead"},
            {'description': 'Draymond Green Takes an in-depth look at Destiny 2', 'reviewer': 7, 'created_on': '2017-10-29 21:15:16.529267', 'id': 11, 'normalized_score': 61, 'score': 11, 'game': 4, 'title': "Draymond Green's Review of Destiny 2"},
            {'description': 'Stephen Curry Takes an in-depth look at Super Smash Bros. for Wii U', 'reviewer': 4, 'created_on': '2017-10-29 21:15:16.529267', 'id': 14, 'normalized_score': 97, 'score': 14, 'game': 5, 'title': "Stephen Curry's Review of Super Smash Bros. for Wii U"},
            {'description': 'Kevin Durant Takes an in-depth look at Super Smash Bros. for Wii U', 'reviewer': 5, 'created_on': '2017-10-29 21:15:16.529267', 'id': 17, 'normalized_score': 88, 'score': 17, 'game': 5, 'title': "Kevin Durant's Review of Super Smash Bros. for Wii U"},
            {'description': 'LeBron James Takes an in-depth look at Assassins Creed Origins', 'reviewer': 8, 'created_on': '2017-10-29 21:15:16.529267', 'id': 3, 'normalized_score': 80, 'score': 3, 'game': 1, 'title': "LeBron James's Review of Assassins Creed Origins"},
            {'description': 'Derrick Rose Takes an in-depth look at Cities Skylines', 'reviewer': 9, 'created_on': '2017-10-29 21:15:16.529267', 'id': 6, 'normalized_score': 80, 'score': 6, 'game': 2, 'title': "Derrick Rose's Review of Cities Skylines"},
            {'description': 'Dwyane Wade Takes an in-depth look at Cuphead', 'reviewer': 10, 'created_on': '2017-10-29 21:15:16.529267', 'id': 9, 'normalized_score': 60, 'score': 9, 'game': 3, 'title': "Dwyane Wade's Review of Cuphead"},
            {'description': 'LeBron James Takes an in-depth look at Destiny 2', 'reviewer': 8, 'created_on': '2017-10-29 21:15:16.529267', 'id': 12, 'normalized_score': 40, 'score': 12, 'game': 4, 'title': "LeBron James's Review of Destiny 2"},
            {'description': 'Derrick Rose Takes an in-depth look at Super Smash Bros. for Wii U', 'reviewer': 9, 'created_on': '2017-10-29 21:15:16.529267', 'id': 15, 'normalized_score': 100, 'score': 15, 'game': 5, 'title': "Derrick Rose's Review of Super Smash Bros. for Wii U"},
            {'description': 'Dwyane Wade Takes an in-depth look at Super Smash Bros. for Wii U', 'reviewer': 10, 'created_on': '2017-10-29 21:15:16.529267', 'id': 18, 'normalized_score': 80, 'score': 18, 'game': 5, 'title': "Dwyane Wade's Review of Super Smash Bros. for Wii U"}
        ])


if __name__ == '__main__':
    from subprocess import call
    call(["rm", "my_database.db"])
    unittest.main()
