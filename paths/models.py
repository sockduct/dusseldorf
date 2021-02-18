from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.
class ResourceType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    type = models.ForeignKey(
        ResourceType,
        on_delete=models.PROTECT,
        related_name='resources'
    )
    url = models.URLField(max_length=2000)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    resource = models.ForeignKey(
        Resource,
        on_delete=models.PROTECT,
        related_name='subjects'
    )

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    resource = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        related_name='areas'
    )

    def __str__(self):
        return self.name
