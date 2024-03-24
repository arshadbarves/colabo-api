from rest_framework import serializers

from task.serializers import TaskSerializer
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'created_at', 'updated_at', 'created_by', 'collaborators', 'tasks']

class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'created_at', 'updated_at', 'created_by', 'collaborators']