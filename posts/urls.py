from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='posts-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='posts-detail'),
    path('comments/', views.CommentListView.as_view(), name='comments-list'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comments-detail'),
]

# router = SimpleRouter()
# router.register('posts', views.PostViewset, basename='posts')
# router.register('comments', views.CommentViewset, basename='comments')

# urlpatterns = router.urls