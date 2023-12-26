
from django.db import transaction
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.views import TokenViewBase

from users.models import User
from users.serializers import UserModelSerializer, RegisterSerializer


class CustomTokenObtainPairView(TokenViewBase):
    """
    login ya'ni access va refresh token

    ```
    """

    _serializer_class = api_settings.TOKEN_OBTAIN_SERIALIZER


class CustomTokenRefreshView(TokenViewBase):
    """
    access token olish from refresh token

    ```
    """

    _serializer_class = api_settings.TOKEN_REFRESH_SERIALIZER


class UserViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    # @action(['post'], False, serializer_class=RegisterSerializer)
    # def register(self, request):
    #     """
    #     ro'yxatdan o'tish
    #
    #     ```
    #     """
    #     try:
    #         with transaction.atomic():
    #             serializer = self.serializer_class(data=request.data)
    #             serializer.is_valid(raise_exception=True)
    #             username = serializer.data.get('username')
    #             password = serializer.data.get('password')
    #             User.objects.create()
