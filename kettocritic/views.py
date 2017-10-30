import collections
from kettocritic import models, serializers

class ModelView():
    model = None
    serializer_class = None
    select_query = None
    filters = []

    def _filter_query(self, query):
        if query is None:
            return None

        result = query
        for f in self.filters:
            result = f(query)
        return result

    def _serialize_query(self, query):
        if self.serializer_class is None or query is None:
            return None
        if not query:
            return []
        
        serializer = self.serializer_class()
        if isinstance(query, collections.Iterable):
            return list(map(serializer.get_serialized_model, query))
        else:
            return serializer.get_serialized_model(query)

    def query(self, model_id=None):
        if self.model is None or self.select_query is None or self.serializer_class is None:
            return None
        
        filtered_query = self._filter_query(self.select_query)
        if model_id:
            filtered_query = filtered_query.where(self.model.id == model_id).first()
        return self._serialize_query(filtered_query)


class GameView(ModelView):
    model = models.Game
    serializer_class = serializers.GameSerializer
    select_query = models.Game.select()


class TeamView(ModelView):
    model = models.Team
    serializer_class = serializers.TeamSerializer
    select_query = models.Team.select()


class ReviewerView(ModelView):
    model = models.Reviewer
    serializer_class = serializers.ReviewerSerializer
    select_query = models.Reviewer.select()


class ReviewView(ModelView):
    model = models.Review
    serializer_class = serializers.ReviewSerializer
    select_query = models.Review.select()
