from rest_framework.fields import CurrentUserDefault, HiddenField
from rest_framework.serializers import ModelSerializer

from todo.models import ToDoWoo


class TodoWooModelSerializer(ModelSerializer):
    author = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = ToDoWoo
        fields = ('id', 'title', 'description', 'author', 'is_important')


class TodoSerializer(ModelSerializer):
    class Meta:
        model = ToDoWoo
        fields = ('id', 'title', 'description', 'is_important', 'is_complete', 'completed_at')
