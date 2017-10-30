from kettocritic import views

class Router(object):
    game_view = views.GameView() 
    team_view = views.TeamView()
    reviewers_view = views.ReviewerView()
    reviews_view = views.ReviewView()

    def get_games(self, game_id=None):
        return self.game_view.query(game_id)

    def get_teams(self, team_id=None):
        return self.team_view.query(team_id)

    def get_reviewers(self, reviewer_id=None):
        return self.reviewers_view.query(reviewer_id)

    def get_reviews(self, review_id=None):
        return self.reviews_view.query(review_id)


