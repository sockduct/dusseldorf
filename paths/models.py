from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.
class ResourceType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # Don't want to allow Null - want all posts to select a type.  That means
    # we must have a default.  For now, just setting to 1 but there may be a
    # better solution:
    type = models.ForeignKey(
        ResourceType,
        on_delete=models.PROTECT,
        related_name='resources',
        default=1
    )
    url = models.URLField(max_length=2000, blank=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    resource = models.ForeignKey(
        Resource,
        on_delete=models.PROTECT,
        related_name='subjects',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    resource = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        related_name='areas',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('path_detail', args=[str(self.id)])
