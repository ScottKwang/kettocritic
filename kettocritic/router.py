import os
from pprint import PrettyPrinter
import sys

from kettocritic import views


class Router(object):
    game_view = views.GameView() 
    team_view = views.TeamView()
    reviewers_view = views.ReviewerView()
    reviews_view = views.ReviewView()

    def _print_dict(self, dictionary):
        printer = PrettyPrinter(indent=4)
        printer.pprint(dictionary)

    def print_games(self, game_id=None, filters={}, sorts=[]):
        self._print_dict(self.get_games(game_id=game_id, filters=filters, sorts=sorts))

    def get_games(self, game_id=None, filters={}, sorts=[]):
        return self.game_view.query(game_id, filters, sorts)

    def print_teams(self, team_id=None, filters={}, sorts=[]):
        self._print_dict(self.get_teams(team_id=team_id, filters=filters, sorts=sorts))

    def get_teams(self, team_id=None, filters={}, sorts=[]):
        return self.team_view.query(team_id, filters, sorts)

    def print_reviewers(self, reviewer_id=None, filters={}, sorts=[]):
        self._print_dict(self.get_reviewers(reviewer_id=reviewer_id, filters=filters, sorts=sorts))

    def get_reviewers(self, reviewer_id=None, filters={}, sorts=[]):
        return self.reviewers_view.query(reviewer_id, filters, sorts)

    def print_reviews(self, review_id=None, filters={}, sorts=[]):
        self._print_dict(self.get_reviews(review_id=review_id, filters=filters, sorts=sorts))

    def get_reviews(self, review_id=None, filters={}, sorts=[]):
        return self.reviews_view.query(review_id, filters, sorts)
