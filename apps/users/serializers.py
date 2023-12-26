from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer

from users.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class RegisterSerializer(Serializer):
    username = serializers.CharField(max_length=300)
    password = serializers.CharField(max_length=300)

    def validate(self, attrs):
        username = attrs.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Bu username allaqachon ishlatilgan !', 404)
        return attrs
