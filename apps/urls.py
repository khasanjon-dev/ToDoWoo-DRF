from django.urls import path, include

urlpatterns = [
    path('user/', include('users.urls')),
    path('todo/', include('todo.urls'))
]
