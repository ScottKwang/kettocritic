import collections
from kettocritic import models, serializers

class ModelView():
    model = None
    serializer_class = None

    def _filter_query(self, query, filters):
        if not filters:
            return query

        result = query
        for field, value in filters.items():
            result = query.where(getattr(self.model, field) == value)
        return result

    def _sort_query(self, query, sorts):
        if not sorts:
            return query

        result = query
        for field in sorts:
            result = query.order_by(getattr(self.model, field))
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

    def query(self, id=None, filters={}, sorts=[]):
        if self.model is None or self.serializer_class is None:
            return None

        query = self.model.select()

        if id:
            object = query.where(self.model.id == id).first()
            return self._serialize_query(object)
        
        filtered_query = self._filter_query(query, filters)
        sorted_query = self._sort_query(filtered_query, sorts)
        return self._serialize_query(sorted_query)


class GameView(ModelView):
    model = models.Game
    serializer_class = serializers.GameSerializer


class TeamView(ModelView):
    model = models.Team
    serializer_class = serializers.TeamSerializer


class ReviewerView(ModelView):
    model = models.Reviewer
    serializer_class = serializers.ReviewerSerializer


class ReviewView(ModelView):
    model = models.Review
    serializer_class = serializers.ReviewSerializer
