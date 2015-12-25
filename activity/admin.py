from django.contrib import admin
from activity.models import Activity, Task, Actor


class ActorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'student_id', 'sex', 'level', 'tel', 'alternative_content')


class TaskAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name', 'responsible_user', 'is_finished', 'is_completed')
    list_display = ('name', 'responsible_user', 'description', 'is_finished', 'is_completed', 'comments')


class ActivityAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('title', 'content', 'entry_closing_time', 'start_time', 'closing_time')
    list_display = ('title', 'content', 'entry_closing_time', 'start_time', 'closing_time', 'is_alternative',
                    'alternative_title')


admin.site.register(Actor, ActorAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Activity, ActivityAdmin)
