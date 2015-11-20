from django.contrib import admin
from carousel.models import Carousel


class CarouselAdmin(admin.ModelAdmin):
    search_fields = ('title', 'summery')
    list_filter = ('title', 'summery', 'target_url', 'show_order', 'on_show', 'create_time')
    list_display = ('title', 'summery', 'target_url', 'show_order', 'on_show', 'create_time')


admin.site.register(Carousel, CarouselAdmin)
