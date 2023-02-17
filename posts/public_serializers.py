from rest_framework import serializers


class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    full_name = serializers.CharField(source='get_full_name', read_only=True)


class PostPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    image = serializers.CharField(read_only=True)
    caption = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)