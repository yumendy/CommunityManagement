from django.contrib import admin
from models import Link


class LinkAdmin(admin.ModelAdmin):
    search_fields = ('name', 'title', 'url',)
    list_display = ('title', 'name', 'url', 'show_order')

admin.site.register(Link, LinkAdmin)
