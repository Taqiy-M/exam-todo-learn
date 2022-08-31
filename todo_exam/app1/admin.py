from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *
# Register your models here.

admin.site.register(Student)


@admin.register(Todo)
class TodoAdmin(ModelAdmin):
    list_display = ('title', 'description')
    list_editable = ('description',)
    search_fields = ('title', 'description')