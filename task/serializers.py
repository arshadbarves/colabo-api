from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'created_date', 'updated_date', 'due_date', 'priority',
                  'status', 'created_by', 'assigned_to']
