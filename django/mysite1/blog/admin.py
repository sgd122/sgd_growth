from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["id", "title", "created_ad"]
    # list_editable = ["title"]
    list_display_links = ["title"]


admin.site.register(Post, PostAdmin)
