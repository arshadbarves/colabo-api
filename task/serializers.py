from rest_framework import serializers

from account.serializers import UserLoginSerializer
from .models import Task, TaskPriority, TaskStatus


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserLoginSerializer(read_only=True)
    created_by = UserLoginSerializer(read_only=True)
    priority = serializers.StringRelatedField()
    status = serializers.StringRelatedField()
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'created_date', 'updated_date', 'due_date', 'priority',
                  'status', 'created_by', 'assigned_to']

class TaskPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPriority
        fields = ['id', 'name']


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ['id', 'name']
        