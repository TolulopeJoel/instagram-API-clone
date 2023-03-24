from rest_framework import serializers

from comments.serializers import CommentListSerializer

from .models import Post, Like
from .public_serializers import UserPublicSerializer


class PostListSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='posts-detail',
        lookup_field ='pk',
    )

    class Meta:
        model = Post
        fields = (
            'user',
            'image',
            'caption',
            'url',
        )


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    image = serializers.ImageField(read_only=True)
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'image',
            'caption',
            'comments',
        )


class LikeSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']