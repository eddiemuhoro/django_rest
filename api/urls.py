from .views import get_users, create_user, get_blog_posts, create_blog_post, update_blog_post
from django.urls import path

urlpatterns=  [
    path('users/', get_users, name='get_user'),
    path('users/create/', create_user, name='create_user'),
    path('blogposts/', get_blog_posts, name='get_blog_posts'),
    path('blogposts/create/', create_blog_post, name='create_blog_post'),
    path('blogposts/<int:pk>/', update_blog_post, name='update_blog_post'),
    path('blogposts/<int:pk>/delete/', update_blog_post, name='delete_blog_post'),
]