from rest_framework import generics

from .models import Post
from .serializers import PostDetailSerializer, PostListSerializer


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
