from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    # Believe makes more sense in Post model because would add/remove tags
    # from the post
    # posts = models.ManyToManyField(Post, related_name='tags')

    def __str__(self):
        return self.name

    '''
    def get_absolute_url(self):
        return reverse('post_list')
    '''

class PostType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    '''
    def get_absolute_url(self):
        return reverse('post_list')
    '''

class Post(models.Model):
    # Don't want to allow Null - want all posts to select a type.  That means
    # we must have a default.  For now, just setting to 1 but there may be a
    # better solution:
    type = models.ForeignKey(
        PostType,
        on_delete=models.PROTECT,
        related_name='posts',
        default=1
    )
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='posts'
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    viewed = models.DateTimeField(null=True, blank=True)
    #
    # Allow multiple tags:
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # This name lines up with the name= in urls.py:
        return reverse('post_detail', args=[str(self.id)])
        # Note - self.id matches the object primary key (pk)
        # When posting, redirect is to this view

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.body[:75]}...'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.post.id)])
