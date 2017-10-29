import unittest

import . from models


class FailingTests(unittest.TestCase):

    def setUp(self):
        """
        Set up fixtures.
        """
        pass

    def reviewer_view_get_test(self):
        """
        `ReviewersView.get()` is returning a list of reviews with missing ’date’ and ’description’ fields.
        Fix the `get` function so it correctly includes the ‘date’ and ‘description’ fields.
        """
        pass

    def game_view_get_with_sort_test(self):
        """
        `GameView.get(sort=‘team’)` isn’t correctly sorting the list of games by team name.
        Fix the `get` function so it correctly sorts the list of games by related team name.
        """
        pass

    def review_view_get_with_filter_test(self):
        """
        `Review.get(filter=‘average_score_gte=70’)` isn’t correctly filtering the list of reviews to only
        include reviews with an average score below 70.
        Fix the `get` function so it correctly filters the list of reivews by average score.
        """
        pass



if __name__ == '__main__':
    unittest.main()
