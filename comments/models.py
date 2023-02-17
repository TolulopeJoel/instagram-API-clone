from django.db import models
from django.contrib.auth import get_user_model

from posts.models import Post


class Comment(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)