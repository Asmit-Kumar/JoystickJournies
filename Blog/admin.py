from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","slug","author",
                    "publish","status", 'genres']
    list_filter = ["status","created","publish",
                   "author", 'genres']
    search_fields = ["title","body"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ["status","publish"]
    

