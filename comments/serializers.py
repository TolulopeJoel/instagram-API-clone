from rest_framework import serializers

from posts.public_serializers import PostPublicSerializer, UserPublicSerializer

from .models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    post = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'post',
            'text',
        )


class CommentDetailSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    post = PostPublicSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'post',
            'text',
        )
