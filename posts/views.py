from rest_framework import generics

from .filters import PostFilter
from .models import Post
from .serializers import PostDetailSerializer, PostListSerializer


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filterset_class = PostFilter


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


