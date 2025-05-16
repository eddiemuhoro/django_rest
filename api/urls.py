from .views import get_users, create_user
from django.urls import path

urlpatterns=  [
    path('users/', get_users, name='get_user'),
    path('users/create/', create_user, name='create_user'),
]