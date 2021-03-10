from config.settings import ADMIN_EMAIL
from django import forms
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect

class PagesContactForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def send_email(self, email):
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        from_email = email

        try:
            send_mail(subject, message, from_email, [settings.ADMIN_EMAIL])
        except BadHeaderError:
            return redirect('error')
