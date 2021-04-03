from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import UserType

CustomUser = get_user_model()

# Register your models here.
class UserTypeAdmin(ModelAdmin):
    model = UserType

# Extend UserAdmin class to use our custom user model:
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # inlines = [UserTypeInline]
    # Not sure if needed since these defined in imported forms:
    list_display = ['email', 'username', 'name', 'nickname', 'type']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name', 'nickname', 'type')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name', 'nickname', 'type')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserType, UserTypeAdmin)
