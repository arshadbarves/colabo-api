from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'due_date', 'priority', 'status', 'created_by')
    list_filter = ('project', 'due_date', 'priority', 'status', 'created_by')
    search_fields = ('title', 'description')


admin.site.register(Task, TaskAdmin)
