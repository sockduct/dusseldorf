from typing import List
from django.contrib.auth import get_user_model
from django.db.models import Count, F
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView

from .forms import PagesContactForm

# Create your views here.
class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(FormView):
    template_name = 'contact.html'
    form_class = PagesContactForm
    success_url = '/success/'

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return HttpResponse('Unauthorized', status=401)

        form.send_email(self.request.user.email)
        return super().form_valid(form)

class ErrorPageView(TemplateView):
    template_name = 'error.html'

class LeaderboardPageView(ListView):
    model = get_user_model()
    '''
    The following QuerySet is close to this, but not exactly the same:
    select username, email,
        ( select 10 * count(*) from posts_post where accounts_customuser.id = posts_post.author_id ) +
        ( select count(*) from posts_comment where accounts_customuser.id = posts_comment.author_id ) total
        from accounts_customuser
        order by total desc, username;

    I believe there are some cases where this won't produce the desired ordering - e.g., 1 post,
    1 comment would be ordered before 0 posts, 12 comments even though the latter should be first.
    '''
    queryset = get_user_model().objects.annotate(
                post_count=Count('posts'),
                comment_count=Count('comment'),
                total=F('post_count') * 10 + F('comment_count')
                ).order_by('-post_count', '-comment_count', 'username')
    template_name = 'leaderboard.html'

class SuccessPageView(TemplateView):
    template_name = 'success.html'
