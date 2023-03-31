from tasks.models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):

    class Meta():
        model = Task
        fields = [
            'title',
            'complete',
            'created',
        ]
    
    def validate(self, data):
        if '#' in data['title']:
            raise serializers.ValidationError({
                'title': "Title can not contain '#'."
            })
        return data

    def update(self, instance, validated_data):
        instance.title = self.validated_data.get('title', instance.title).capitalize()
        instance.save()
        return instance
