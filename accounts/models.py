from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class UserType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    class Meta:
        ordering = ['username']

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
    # Replacement:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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

    def __str__(self):
        return self.username

    ''' When eventually create user detail page to allow updates:
    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])
    '''
