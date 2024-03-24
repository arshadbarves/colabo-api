from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    collaborators = models.ManyToManyField(User, related_name='projects_collaborated')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Projects'
