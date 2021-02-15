from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        # model = get_user_model()
        model = CustomUser
        # Password field included by default!
        # Could add more fields, see:
        # https://docs.djangoproject.com/en/3.1/ref/contrib/auth/
        fields = ('email', 'username', 'name', 'nickname')
        # Alternatively:
        # fields = UserCreationForm.Meta.fields + ('age',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        # Looks to AUTH_USER_MODEL in config/settings.py:
        # model = get_user_model()
        model = CustomUser
        fields = ('email', 'username', 'name', 'nickname')
        # Alternatively:
        # fields = UserChangeForm.Meta.fields
