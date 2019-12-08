from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'priority_level', 'date_created', 'date_updated')