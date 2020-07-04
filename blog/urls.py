from django.urls import path
from .views import (
    blog_post_list_view,
    blog_post_create_view,
    blog_post_detail_view,
    blog_post_update_view,
    blog_post_delete_view,
)

app_name ='blog'
urlpatterns = [
    path('', blog_post_list_view, name='blog-list'),
    path('blog-new/', blog_post_create_view, name='blog-create'),
    path('<slug:slug>/', blog_post_detail_view, name='blog-detail'),
    path('<slug:slug>/edit/', blog_post_update_view, name='blog-update'),
    path('<slug:slug>/delete/', blog_post_delete_view, name='blog-delete'),
]
