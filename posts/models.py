from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.caption
