from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # Password field included by default!
        # Could add more fields, see:
        # https://docs.djangoproject.com/en/3.1/ref/contrib/auth/
        fields = ('email', 'username',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        # Looks to AUTH_USER_MODEL in config/settings.py:
        model = get_user_model()
        fields = ('email', 'username',)
