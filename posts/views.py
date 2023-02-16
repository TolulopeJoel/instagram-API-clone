from rest_framework import generics
from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)
