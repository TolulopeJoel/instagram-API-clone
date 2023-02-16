from rest_framework import serializers

from .models import Post


class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)


class PostSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='posts-detail',
        lookup_field ='pk',
    )

    class Meta:
        model = Post
        fields = (
            'user',
            'caption',
            'image',
            'url',
        )
