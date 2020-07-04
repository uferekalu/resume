from django.urls import path
from .views import (
    BlogPostCreateAPIView,
    BlogPostListAPIView,
    BlogPostDeleteAPIView,
    BlogPostDetailAPIView,
    BlogPostUpdateAPIView,
)

app_name = 'api'
urlpatterns = [
    path('', BlogPostListAPIView.as_view(), name='blog-list'),
    path('create/', BlogPostCreateAPIView.as_view(), name='create'),
    path('<slug:slug>/', BlogPostDetailAPIView.as_view(), name='blog-detail'),
    path('<slug:slug>/edit/', BlogPostUpdateAPIView.as_view(), name='blog-update'),
    path('<slug:slug>/delete/', BlogPostDeleteAPIView, name='blog-delete'),
]
