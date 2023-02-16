from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
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
