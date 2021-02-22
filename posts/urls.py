from django.urls import path

from .views import PostDetailView, PostListView

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
]
