from rest_framework import generics, status
from rest_framework.response import Response

from accounts.mixins import UserQuerySetMixin

from .filters import PostFilter
from .models import Like, Post
from .serializers import LikeSerializer, PostDetailSerializer, PostListSerializer


class PostListView(generics.ListCreateAPIView):
    """
    API view for listing and creating posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filterset_class = PostFilter

    def perform_create(self, serializer):
        """
        Create a new post with the current user as the owner.
        """
        user = self.request.user
        return serializer.save(user=user)


class PostDetailView(UserQuerySetMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific post.
    """
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class LikeListView(generics.ListCreateAPIView):
    """
    API view for listing and creating likes for posts.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        """
        Create a new like for a post.
        Returns:
            Response with the serialized Like object or error if post_id is invalid.
        """
        post_id = request.data.get('post_id')
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

        like = Like(user=request.user, post=post)
        like.save()

        return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)


class LikeDetailView(UserQuerySetMixin, generics.RetrieveDestroyAPIView):
    """
    API view for retrieving and deleting a specific like.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
