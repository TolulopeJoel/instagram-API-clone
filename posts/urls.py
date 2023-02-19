from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='posts-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='posts-detail'),
    path('posts/<int:pk>/like/', views.PostDetailView.as_view(), name='like'),
    path('posts/<int:pk>/unlike/', views.PostDetailView.as_view(), name='unlike'),
]
