from rest_framework import serializers

from .models import Post
from comments.serializers import CommentListSerializer


class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    full_name = serializers.CharField(source='get_full_name', read_only=True)


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
    comments = CommentListSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'user',
            'image',
            'caption',
            'comments',
        )