from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import MyUser, Department


class MyUserInline(admin.StackedInline):
    model = MyUser
    can_delete = False


class MyUserAdmin(UserAdmin):
    inlines = (MyUserInline,)


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(Department, DepartmentAdmin)
