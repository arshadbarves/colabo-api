from rest_framework import permissions, viewsets
from project.pagination import CustomPagination
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsCollaboratorOrReadOnly

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCollaboratorOrReadOnly]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Task.objects.none()
        return Task.objects.filter(created_by=user) | Task.objects.filter(project__collaborators=user)