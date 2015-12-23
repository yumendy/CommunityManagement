from django.contrib import admin
from announcement.models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    search_fields = ('content',)
    list_filter = ('author', 'create_time')
    list_display = ('author', 'create_time', 'content')


admin.site.register(Announcement, AnnouncementAdmin)
