from rest_framework import serializers

from .models import Post, Comment


class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    full_name = serializers.CharField(source='get_full_name', read_only=True)


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'text',
        )


class PostSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    comments = CommentSerializer(many=True)
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
            'comments',
        )
