from django.contrib import admin

from .models import Comment, Post, PostType, Tag

# Register your models here.
''' # Don't believe I want/need this:
class TagInline(admin.TabularInline):
    model = Tag.posts.through
    # Default = display 3 extra (emptry) rows:
    extra = 1
'''

class TagAdmin(admin.ModelAdmin):
    model = Tag

class PostTypeAdmin(admin.ModelAdmin):
    model = PostType

class CommentAdmin(admin.ModelAdmin):
    model = Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [CommentInline, ]

admin.site.register(PostType, PostTypeAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
