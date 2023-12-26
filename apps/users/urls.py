from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import CustomTokenObtainPairView, CustomTokenRefreshView, UserViewSet

router = DefaultRouter()
router.register('', UserViewSet, 'user')
urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='refresh'),
    path('', include(router.urls))
]
