from rest_framework import serializers

from .models import Comment

class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'text',
        )


class CommentDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'text',
        )
