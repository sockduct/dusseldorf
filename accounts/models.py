from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UserType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)

class CustomUser(AbstractUser):
    # null=True - allow database field to have a NULL value
    # blank=True - allow form field to have blank value
    # Above two often used together
    # Note - doesn't always make sense to use Null, depends on the database
    #        field type.  For strings, often times '' is better.
    #
    # Default fields:
    # Username
    # Password
    # First name
    # Last name
    # Email address
    # Active (account enabled)
    # Staff status (e.g., part of IT)
    # Superuser status (e.g., admin)
    # Group memberships
    # User permissions
    # Last login
    # Date joined
    #
    # Example:
    # age = models.PositiveIntegerField(null=True, blank=True)
    #
    # Adds:
    name = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(max_length=25, blank=True)
    #
    # UserType:  e.g., student, professional, hobbyist, ...:
    type = models.ForeignKey(
        UserType,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='users'
    )
