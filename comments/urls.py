from django.urls import path

from . import views

urlpatterns = [
    path('', views.CommentListView.as_view(), name='comments-list'),
    path('<int:pk>/', views.CommentDetailView.as_view(), name='comments-detail'),
]
