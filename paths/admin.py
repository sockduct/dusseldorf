from django.contrib import admin

from .models import Area, Subject, Resource, ResourceType

# Register your models here.
class ResourceTypeAdmin(admin.ModelAdmin):
    model = ResourceType

class ResourceAdmin(admin.ModelAdmin):
    model = Resource

class SubjectAdmin(admin.ModelAdmin):
    model = Subject

class AreaAdmin(admin.ModelAdmin):
    model = Area

admin.site.register(ResourceType, ResourceTypeAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Area, AreaAdmin)
