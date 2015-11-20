from django.contrib import admin
from navbar.models import NavItem


class NavItemAdmin(admin.ModelAdmin):
    search_fields = ('title', 'url',)
    list_filter = ('title', 'create_time')
    list_display = ('title', 'show_order', 'url', 'create_time')


admin.site.register(NavItem, NavItemAdmin)
