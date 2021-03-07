# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Post, PostType

# Create your views here.
class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['type', 'title', 'body', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['type', 'title', 'body', 'tags']

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
