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
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully", "data": serializer.data}, status=201)
    else:
        return Response({"error": serializer.errors}, status=400)

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

@api_view(['PUT', 'DELETE'])
def update_blog_post(request, pk):
    try:
        blog_post = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return Response({"error": "Blog post not found"}, status=404)

    if request.method == 'PUT':
        serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Blog post updated successfully", "data": serializer.data}, status=200)
        else:
            return Response({"error": serializer.errors}, status=400)

    elif request.method == 'DELETE':
        blog_post.delete()
        return Response({"message": "Blog post deleted successfully"}, status=204)