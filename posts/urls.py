from django.urls import path

from .views import AboutPageView, PostDetailView, PostListView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
]
