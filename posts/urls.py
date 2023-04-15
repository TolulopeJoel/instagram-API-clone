from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts-list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='posts-detail'),
    path('<int:pk>/like/', views.LikeListView.as_view(), name='like'),
    path('<int:pk>/unlike/', views.LikeDetailView.as_view(), name='unlike'),
]
