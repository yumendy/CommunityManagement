from django.contrib import admin
from article.models import Category, Blog, PurePage


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


class BlogAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_filter = ('author', 'category', 'publish_time', 'modification_time')
    list_display = ('title', 'author', 'category', 'publish_time', 'modification_time', 'show_times',)


class PurePageAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_filter = ('publish_time', 'modification_time')
    list_display = ('title',  'publish_time', 'modification_time', 'show_times',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(PurePage, PurePageAdmin)
