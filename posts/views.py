from rest_framework import generics, status
from rest_framework.response import Response

from accounts.mixins import UserQuerySetMixin

from .filters import PostFilter
from .models import Like, Post
from .serializers import (
    PostDetailSerializer,PostListSerializer,
    LikeSerializer, 
)


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filterset_class = PostFilter


class PostDetailView(UserQuerySetMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class LikeListView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

        like = Like(user=request.user, post=post)
        like.save()

        return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)


class LikeDetailView(UserQuerySetMixin, generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
