# from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Post, PostType

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
