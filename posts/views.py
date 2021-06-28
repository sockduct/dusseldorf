from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.db.models import query
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Comment, Post, PostType

# Create your views here.
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ['body']
    # Appears to work, but if wanted to be explicit:
    # login_url = 'account_login' # Django-allauth login, default is 'login'

    def form_valid(self, form):
        post_id = self.request.path.split('/')[2]
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=post_id)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.request.path.split('/')[2]
        context['post'] = Post.objects.get(id=post_id)
        return context

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post_id})

    def test_func(self):
        obj = self.get_object()
        return self.request.user.is_staff or self.request.user == obj.author

class CommentEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'comment_edit.html'
    fields = ['body']

    def test_func(self):
        obj = self.get_object()
        return self.request.user.is_staff or self.request.user == obj.author

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['type', 'title', 'body', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return self.request.user.is_staff or self.request.user == obj.author

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    # Optional - choose friendlier name:
    # context_object_name = 'post'
    # Note - default context_object_name is 'object'

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['type', 'title', 'body', 'tags']

    def test_func(self):
        obj = self.get_object()
        return self.request.user.is_staff or self.request.user == obj.author

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    # Optional - choose friendlier name:
    # context_object_name = 'post_list'
    # Note - default context_object_name is 'object_list'

class SearchResultsListView(ListView):
    model = Post
    template_name = 'search_results.html'

    # Can either use queryset = ...
    # queryset = Post.objects.filter(title__icontains='welcome')
    #
    # Or define get_queryset function:
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
            # "|" acts as "or" operator for Q:
            Q(title__icontains=query) | Q(tags__name__contains=query)
        )
