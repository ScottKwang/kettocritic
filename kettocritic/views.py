from kettocritic import models, serializers

class ModelView():
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

    def _serialize_results(self, results):
        if self.serializer_class is None:
            return None
        
        serializer = self.serializer_class()
        return list(map(serializer.get_serialized_model, results))

    def query(self):
        if self.select_query is None:
            return
        if self.serializer_class is None:
            return
        
        filtered_results = self._filter_query(self.select_query)
        serialized_results = self._serialize_results(filtered_results)
        print(serialized_results)


class GameView(ModelView):
    serializer_class = serializers.GameSerializer
    select_query = models.Game.select()


class TeamView(ModelView):
    serializer_class = serializers.TeamSerializer
    select_query = models.Team.select()


class ReviewerView(ModelView):
    serializer_class = serializers.ReviewerSerializer
    select_query = models.Reviewer.select()


class ReviewView(ModelView):
    serializer_class = serializers.ReviewSerializer
    select_query = models.Review.select()
