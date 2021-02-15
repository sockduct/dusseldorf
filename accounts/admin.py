from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import UserType

CustomUser = get_user_model()

class UserTypeInline(admin.TabularInline):
    model = UserType
    # Default - display 3 extra (empty) rows:
    extra = 1

# Register your models here.
# Extend UserAdmin class to use our custom user model:
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    inlines = [UserTypeInline]
    # Not sure if needed since these defined in imported forms:
    list_display = ['email', 'username', 'name', 'nickname']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name', 'nickname',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name', 'nickname',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
