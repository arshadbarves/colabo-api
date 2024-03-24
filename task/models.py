from django.db import models
from django.contrib.auth.models import User
from project.models import Project


class TaskStatus(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Task statuses'


class TaskPriority(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Task priorities'


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.ForeignKey(TaskPriority, on_delete=models.PROTECT)
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.SET_NULL, null=True,
                                    blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['due_date']
        verbose_name_plural = 'Tasks'
