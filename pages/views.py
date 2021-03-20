from typing import List
from django.contrib.auth import get_user_model
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
        form.send_email(self.request.user.email)
        return super().form_valid(form)

class ErrorPageView(TemplateView):
    template_name = 'error.html'

class LeaderboardPageView(ListView):
    model = get_user_model()
    template_name = 'leaderboard.html'

class SuccessPageView(TemplateView):
    template_name = 'success.html'
