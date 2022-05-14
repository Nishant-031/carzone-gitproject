from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnails(self, objects):
        return format_html('<img src= "{}" width= "40" style= "border-radius: 50px;" />'.format(objects.photos.url))
    thumbnails.short_description = 'Photo'

    list_display = ('id','thumbnails', 'full_name', 'desination')
    list_display_links= ('id', 'thumbnails', 'full_name')
    search_fields= ('id', 'first_name', 'desination')
    list_filter = ('desination',)

admin.site.register(Team, TeamAdmin)
