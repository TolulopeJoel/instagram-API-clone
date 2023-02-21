from rest_framework import generics, status
from rest_framework.response import Response

from .filters import PostFilter
from .models import Post, Like
from .serializers import LikeSerializer, PostDetailSerializer, PostListSerializer


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filterset_class = PostFilter


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
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


class LikeDetailView(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
