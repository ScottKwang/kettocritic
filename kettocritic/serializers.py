class ModelSerializer():
    fields = []

    def _get_serialized_field(self, instance, field):
        # if get function found, return result of get function
        # otherwise try to return string of field?
        try:
            getter = 'get_%s' % field
            return self.__getattribute__(getter)(instance)
        except AttributeError:
            pass

        try:
            return getattr(instance, field)
        except AttributeError:
            return

    def get_serialized_model(self, instance):
        serialized_data = {}
        for field in self.fields:        
            serialized_data[field] = self._get_serialized_field(instance, field)
        return serialized_data
        

class GameSerializer(ModelSerializer):
    fields = ['name']


class TeamSerializer(ModelSerializer):
    fields = ['name', 'website']


class ReviewerSerializer(ModelSerializer):
    fields = ['name', 'team']


class ReviewSerializer(ModelSerializer):
    fields = ['created_on', 'description', 'game', 'reviewer', 'score', 'title']
