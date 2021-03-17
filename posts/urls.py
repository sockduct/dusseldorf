from django.urls import path

from .views import (
    CommentCreateView, CommentDeleteView, CommentEditView,
    PostCreateView, PostDeleteView, PostDetailView, PostEditView, PostListView
)

urlpatterns = [
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='comment_new'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
]
