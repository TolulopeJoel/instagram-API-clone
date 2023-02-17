from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('posts', views.PostViewset, basename='posts')
router.register('comments', views.CommentViewset, basename='comments')

urlpatterns = router.urls