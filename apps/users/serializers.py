from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer

from users.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(Serializer):
    username = serializers.CharField(max_length=300)
    password = serializers.CharField(max_length=300)
    confirm_password = serializers.CharField(max_length=300)

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            message = 'Parol bir xil emas !'
            raise ValidationError(message, 404)
        attrs['password'] = make_password(password)
        return attrs
