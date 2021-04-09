from django.urls import path

from .views import (
    CommentCreateView, CommentDeleteView, CommentEditView,
    PostCreateView, PostDeleteView, PostDetailView, PostEditView, PostListView
)

urlpatterns = [
    path('post/comment/<uuid:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('post/comment/<uuid:pk>/edit/', CommentEditView.as_view(), name='comment_edit'),
    path('post/<uuid:pk>/comment/new/', CommentCreateView.as_view(), name='comment_new'),
    path('post/<uuid:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<uuid:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
]
