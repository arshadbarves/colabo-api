from django.contrib import admin

from task.models import Task, TaskPriority, TaskStatus
from .models import Project

class TaskPriorityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(TaskPriority, TaskPriorityAdmin)

class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(TaskStatus, TaskStatusAdmin)

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'created_by')
    list_filter = ('start_date', 'end_date', 'created_by')
    search_fields = ('name', 'description')
    inlines = [TaskInline]

admin.site.register(Project, ProjectAdmin)
