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

    def test_review_view_get(self):
        """
        `router.get_reviews()` is returning a list of reviews with missing 'create_on' and 'description' fields.
        Update the endpoint so that it correctly includes the 'date' and 'description' fields.
        """
        self.assertEqual(router.get_reviews(sorts=['id']), [
            {'description': 'John Wall Takes an in-depth look at Assassins Creed Origins', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 1, 'title': "John Wall's Review of Assassins Creed Origins", 'score': 1, 'game': 1},
            {'description': 'Stephen Curry Takes an in-depth look at Assassins Creed Origins', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 4, 'title': "Stephen Curry's Review of Assassins Creed Origins", 'score': 2, 'game': 1},
            {'description': 'LeBron James Takes an in-depth look at Assassins Creed Origins', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 8, 'title': "LeBron James's Review of Assassins Creed Origins", 'score': 3, 'game': 1},
            {'description': 'Bradley Beal Takes an in-depth look at Cities Skylines', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 2, 'title': "Bradley Beal's Review of Cities Skylines", 'score': 4, 'game': 2},
            {'description': 'Kevin Durant Takes an in-depth look at Cities Skylines', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 5, 'title': "Kevin Durant's Review of Cities Skylines", 'score': 5, 'game': 2},
            {'description': 'Derrick Rose Takes an in-depth look at Cities Skylines', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 9, 'title': "Derrick Rose's Review of Cities Skylines", 'score': 6, 'game': 2},
            {'description': 'Mike Scott Takes an in-depth look at Cuphead', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 3, 'title': "Mike Scott's Review of Cuphead", 'score': 7, 'game': 3},
            {'description': 'Klay Thompson Takes an in-depth look at Cuphead', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 6, 'title': "Klay Thompson's Review of Cuphead", 'score': 8, 'game': 3},
            {'description': 'Dwyane Wade Takes an in-depth look at Cuphead', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 10, 'title': "Dwyane Wade's Review of Cuphead", 'score': 9, 'game': 3},
            {'description': 'John Wall Takes an in-depth look at Destiny 2', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 1, 'title': "John Wall's Review of Destiny 2", 'score': 10, 'game': 4},
            {'description': 'Draymond Green Takes an in-depth look at Destiny 2', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 7, 'title': "Draymond Green's Review of Destiny 2", 'score': 11, 'game': 4},
            {'description': 'LeBron James Takes an in-depth look at Destiny 2', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 8, 'title': "LeBron James's Review of Destiny 2", 'score': 12, 'game': 4},
            {'description': 'Bradley Beal Takes an in-depth look at Super Smash Bros. for Wii U', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 2, 'title': "Bradley Beal's Review of Super Smash Bros. for Wii U", 'score': 13, 'game': 5},
            {'description': 'Stephen Curry Takes an in-depth look at Super Smash Bros. for Wii U', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 4, 'title': "Stephen Curry's Review of Super Smash Bros. for Wii U", 'score': 14, 'game': 5},
            {'description': 'Derrick Rose Takes an in-depth look at Super Smash Bros. for Wii U', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 9, 'title': "Derrick Rose's Review of Super Smash Bros. for Wii U", 'score': 15, 'game': 5},
            {'description': 'Mike Scott Takes an in-depth look at Super Meat Boy', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 3, 'title': "Mike Scott's Review of Super Meat Boy", 'score': 16, 'game': 6},
            {'description': 'Kevin Durant Takes an in-depth look at Super Smash Bros. for Wii U', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 5, 'title': "Kevin Durant's Review of Super Smash Bros. for Wii U", 'score': 17, 'game': 5},
            {'description': 'Dwyane Wade Takes an in-depth look at Super Smash Bros. for Wii U', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 10, 'title': "Dwyane Wade's Review of Super Smash Bros. for Wii U", 'score': 18, 'game': 5}
        ])

    def test_game_view_get_with_filter(self):
        """
        `router.get_games(filter={'average_score_gte': 70})` isn't correctly filtering the list of games
        to only include games with an average score of 70 or greater.
        Update the filtering to correctly filter the list of games by average score.
        Easy Mode: Implement filtering after the objects have been serialized
        Hard Mode: Implement filtering at the ORM level 
        """
        self.assertEqual(router.get_reviews(filters={'average_score_gte': 70}), [
            {'name': 'Assassins Creed Origins'},
            {'name': 'Cuphead'},
            {'name': 'Super Smash Bros. for Wii U'},
            {'name': 'Super Meat Boy'},
        ])

    def test_review_view_get_with_sort(self):
        """
        `GameView.get(sort='team__name')` isn't correctly sorting the list of reviews by reviewer team name.
        Modify the `ModelView` class such that queries can be sorted by related properties.
        Extra Credit: expand related fields so that we are able to see the related teams in the router output
        Note: Test should not fail if you complete the extra credit
        """
        self.assertEqual(router.get_review(sort=['reviewer__team__name', 'id']), [{
            {'description': 'John Wall Takes an in-depth look at Assassins Creed Origins', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 1, 'title': "John Wall's Review of Assassins Creed Origins", 'score': 1, 'game': 1},
            {'description': 'Bradley Beal Takes an in-depth look at Cities Skylines', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 2, 'title': "Bradley Beal's Review of Cities Skylines", 'score': 4, 'game': 2},
            {'description': 'Mike Scott Takes an in-depth look at Cuphead', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 3, 'title': "Mike Scott's Review of Cuphead", 'score': 7, 'game': 3},
            {'description': 'John Wall Takes an in-depth look at Destiny 2', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 1, 'title': "John Wall's Review of Destiny 2", 'score': 10, 'game': 4},
            {'description': 'Bradley Beal Takes an in-depth look at Super Smash Bros. for Wii U', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 2, 'title': "Bradley Beal's Review of Super Smash Bros. for Wii U", 'score': 13, 'game': 5},
            {'description': 'Mike Scott Takes an in-depth look at Super Meat Boy', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 3, 'title': "Mike Scott's Review of Super Meat Boy", 'score': 16, 'game': 6},
            {'description': 'Stephen Curry Takes an in-depth look at Assassins Creed Origins', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 4, 'title': "Stephen Curry's Review of Assassins Creed Origins", 'score': 2, 'game': 1},
            {'description': 'Kevin Durant Takes an in-depth look at Cities Skylines', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 5, 'title': "Kevin Durant's Review of Cities Skylines", 'score': 5, 'game': 2},
            {'description': 'Klay Thompson Takes an in-depth look at Cuphead', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 6, 'title': "Klay Thompson's Review of Cuphead", 'score': 8, 'game': 3},
            {'description': 'Draymond Green Takes an in-depth look at Destiny 2', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 7, 'title': "Draymond Green's Review of Destiny 2", 'score': 11, 'game': 4},
            {'description': 'Stephen Curry Takes an in-depth look at Super Smash Bros. for Wii U', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 4, 'title': "Stephen Curry's Review of Super Smash Bros. for Wii U", 'score': 14, 'game': 5},
            {'description': 'Kevin Durant Takes an in-depth look at Super Smash Bros. for Wii U', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 5, 'title': "Kevin Durant's Review of Super Smash Bros. for Wii U", 'score': 17, 'game': 5},
            {'description': 'LeBron James Takes an in-depth look at Assassins Creed Origins', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 8, 'title': "LeBron James's Review of Assassins Creed Origins", 'score': 3, 'game': 1},
            {'description': 'Derrick Rose Takes an in-depth look at Cities Skylines', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 9, 'title': "Derrick Rose's Review of Cities Skylines", 'score': 6, 'game': 2},
            {'description': 'Dwyane Wade Takes an in-depth look at Cuphead', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 10, 'title': "Dwyane Wade's Review of Cuphead", 'score': 9, 'game': 3},
            {'description': 'LeBron James Takes an in-depth look at Destiny 2', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 8, 'title': "LeBron James's Review of Destiny 2", 'score': 12, 'game': 4},
            {'description': 'Derrick Rose Takes an in-depth look at Super Smash Bros. for Wii U', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 9, 'title': "Derrick Rose's Review of Super Smash Bros. for Wii U", 'score': 15, 'game': 5},
            {'description': 'Dwyane Wade Takes an in-depth look at Super Smash Bros. for Wii U', 'created_on': '2017-10-29 21:15:16.529267', 'reviewer': 10, 'title': "Dwyane Wade's Review of Super Smash Bros. for Wii U", 'score': 18, 'game': 5}
        }])


if __name__ == '__main__':
    from subprocess import call
    call(["rm", "my_database.db"])
    unittest.main()
