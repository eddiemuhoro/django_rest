from rest_framework import serializers
from .models import User  # Assuming you have a User model in models.py

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # or specify the fields you want to include
