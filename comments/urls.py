from django.urls import path

from . import views

urlpatterns = [
    path('comments/', views.CommentListView.as_view(), name='comments-list'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comments-detail'),
]
