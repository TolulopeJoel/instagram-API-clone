from rest_framework import generics, status
from rest_framework.response import Response

from accounts.mixins import UserQuerySetMixin
from posts.models import Post

from .models import Comment
from .serializers import CommentDetailSerializer, CommentListSerializer


class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(
            user=user,
            post_id=self.request.POST.get('pk')
        )
    
    def post(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

        content = request.data.get('content')
        comment = Comment(user=request.user, post=post, content=content)
        comment.save()

        return Response(CommentListSerializer(comment).data, status=status.HTTP_201_CREATED)


class CommentDetailView(UserQuerySetMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
