from django.urls import path

from .views import (
    AreaDetailView, AreaListView,
    SubjectDetailView, SubjectListView,
    ResourceDetailView, ResourceListView
)

urlpatterns = [
    path('area/<int:pk>/', AreaDetailView.as_view(), name='path_detail'),
    path('subject/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('resource/<int:pk>/', ResourceDetailView.as_view(), name='resource_detail'),
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('resources/', ResourceListView.as_view(), name='resource_list'),
    path('', AreaListView.as_view(), name='path_list'),
]
