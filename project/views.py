from rest_framework import permissions, viewsets

from .pagination import CustomPagination
from .models import Project
from .serializers import ProjectSerializer, ProjectListSerializer
from .permissions import IsProjectCreatorOrCollaborator


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectCreatorOrCollaborator]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, collaborators=[self.request.user])

    def get_queryset(self):
        user = self.request.user
        return (Project.objects.filter(collaborators=user) | Project.objects.filter(created_by=user)).distinct()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        return self.serializer_class
