from rest_framework import serializers
from .models import User, BlogPost  # Assuming you have a User model in models.py

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__' 