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
            # {'__gte': operator.gte}
            if field.endswith('__gte'):
                field = field[0:-5]
                result = [instance for instance in query
                          if getattr(instance, field) >= value]
            else:
                result = query.where(getattr(self.model, field) == value)
        return result

    def _sort_query(self, query, sorts):
        if not sorts:
            return query

        result = list(query)
        sorts.reverse()
        for field in sorts:
            field_chain = field.split('__')
            for instance in result:
                instance._sort_value = instance
                for cur_field in field_chain:
                    instance._sort_value = getattr(instance._sort_value, cur_field)
                if isinstance(instance._sort_value, basestring):
                    instance._sort_value = instance._sort_value.lower()

            result.sort(key=lambda elem: elem._sort_value)
            # result = query.order_by(getattr(self.model, field))

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
            query = query.where(self.model.id == id).first()
        else:
            query = self._filter_query(query, filters)
            query = self._sort_query(query, sorts)

        return self._serialize_query(query)


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
