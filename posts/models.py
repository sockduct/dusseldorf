from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.
class PostType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    '''
    def get_absolute_url(self):
        return reverse('post_list')
    '''

class Post(models.Model):
    type = models.ForeignKey(
        PostType, on_delete=models.PROTECT, related_name='posts', null=True, blank=True
    )
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    viewed = models.DateTimeField()
    # What do I need to allow multiple tags?
    # tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    posts = models.ManyToManyField(Post, related_name='tags')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_list')
