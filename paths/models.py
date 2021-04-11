from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Area(models.Model):
    class Meta:
        ordering = ['name']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('path_detail', args=[str(self.id)])

class Subject(models.Model):
    class Meta:
        ordering = ['name']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)
    area = models.ForeignKey(
        Area,
        on_delete=models.PROTECT,
        related_name='subjects',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subject_detail', args=[str(self.id)])

class ResourceType(models.Model):
    class Meta:
        ordering = ['name']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class Resource(models.Model):
    class Meta:
        ordering = ['name']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)
    # Don't want to allow Null - want all posts to select a type.  That means
    # we must have a default.  For now, just setting to 1 but there may be a
    # better solution:
    subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        related_name='resources',
        null=True,
        blank=True
    )
    type = models.ForeignKey(
        ResourceType,
        on_delete=models.PROTECT,
        related_name='resources',
        default=1
    )
    url = models.URLField(max_length=2000, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('resource_detail', args=[str(self.id)])
