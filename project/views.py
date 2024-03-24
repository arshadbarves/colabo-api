from rest_framework import permissions, viewsets

from .pagination import CustomPagination
from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsCollaboratorOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCollaboratorOrReadOnly]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Project.objects.none()
        return Project.objects.filter(created_by=user) | Project.objects.filter(collaborators=user)
