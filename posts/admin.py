from django.contrib import admin

from .models import Post, PostType, Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag.posts.through
    # Default = display 3 extra (emptry) rows:
    extra = 1

class PostTypeAdmin(admin.ModelAdmin):
    model = PostType

class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [TagInline]

admin.site.register(PostType, PostTypeAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
