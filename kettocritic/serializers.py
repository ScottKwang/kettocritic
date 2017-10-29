class ModelSerializer():
    fields = []

    def get_serialized_model(self, instance):
        serialized_data = {}
        for field in self.fields:        
            serialized_data[field] = str(instance.__getattribute__(field))
        return serialized_data
        

class GameSerializer(ModelSerializer):
    fields = ['name']


class TeamSerializer(ModelSerializer):
    fields = ['name', 'website']


class ReviewerSerializer(ModelSerializer):
    fields = ['name', 'team']


class ReviewSerializer(ModelSerializer):
    fields = ['created_on', 'description', 'game', 'reviewer', 'score', 'title']
