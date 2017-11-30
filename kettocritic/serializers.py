import datetime
from kettocritic.models import BaseModel

class ModelSerializer():
    fields = []

    def _get_serialized_field(self, instance, field):
        # if get function found, return result of get function
        # otherwise try to return string of field
        getter_str = 'get_%s' % field
        getter = getattr(self, getter_str, None)
        if getter:
            return getter(instance)

        attr = getattr(instance, field, None)
        if isinstance(attr, BaseModel):
            return attr.id
        if isinstance(attr, datetime.datetime):
            return str(attr)
        return attr

    def get_serialized_model(self, instance):
        serialized_data = {}
        for field in self.fields:
            serialized_data[field] = self._get_serialized_field(instance, field)
        return serialized_data


class GameSerializer(ModelSerializer):
    fields = ['id', 'name', 'average_score']

    def get_average_score(self, instance):
        # TODO
        return 0


class TeamSerializer(ModelSerializer):
    fields = ['id', 'num_reviews', 'num_reviewers']

    def get_num_reviews(self, instance):
        return sum(reviewer.reviews.count() for reviewer in instance.reviewers)

    def get_num_reviewers(self, instance):
        return instance.reviewers.count()


class ReviewerSerializer(ModelSerializer):
    fields = ['id', 'name', 'team']


class ReviewSerializer(ModelSerializer):
    fields = ['id', 'created_on', 'game', 'reviewer', 'title']

    def get_normalized_score(self):
        # TODO
        return 0
