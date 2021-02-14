from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class CustomUser(AbstractUser):
    # null=True - allow database field to have a NULL value
    # blank=True - allow form field to have blank value
    # Above two often used together
    # Note - doesn't always make sense to use Null, depends on the database
    #        field type.  For strings, often times '' is better.
    # age = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(max_length=25, blank=True)
    # e.g., student, professional, hobbyist, ...:
    type = models.IntegerField(null=True, blank=True)

class UserType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    type = models.ForeignKey(
        CustomUser,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
