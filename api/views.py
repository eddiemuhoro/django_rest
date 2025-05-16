from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, BlogPost
from .serializers import UserSerializer, BlogPostSerializer

# Create your views here.
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serialized_users = UserSerializer(users, many=True)
    return Response(serialized_users.data)

@api_view(['POST'])
def create_user(request):
    data = request.data
    # Here you would typically save the user to the database
    return Response({"message": "User created successfully", "data": data})

@api_view(['GET'])
def get_blog_posts(request):
    data = BlogPost.objects.all()
    serialized_data = BlogPostSerializer(data, many=True)
    return Response(serialized_data.data)

@api_view(['POST'])
def create_blog_post(request):
    data = request.data
    serializer = BlogPostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Blog post created successfully", "data": serializer.data}, status=201)
    else:
        return Response({"error": serializer.errors}, status=400)
