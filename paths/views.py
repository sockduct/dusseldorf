# from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import ResourceType, Resource, Subject, Area

# Create your views here.
class AreaListView(ListView):
    model = Area
    template_name = 'path_list.html'

class AreaDetailView(DetailView):
    model = Area
    template_name = 'path_detail.html'

class SubjectListView(ListView):
    model = Subject
    template_name = 'subject_list.html'

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subject_detail.html'

class ResourceListView(ListView):
    model = Resource
    template_name = 'resource_list.html'

class ResourceDetailView(DetailView):
    model = Resource
    template_name = 'resource_detail.html'
