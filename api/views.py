from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User

# Create your views here.
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    print(users)
    return Response({"name": "John Doe", "age": 30})

@api_view(['POST'])
def create_user(request):
    data = request.data
    # Here you would typically save the user to the database
    return Response({"message": "User created successfully", "data": data})