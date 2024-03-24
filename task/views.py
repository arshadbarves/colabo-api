from rest_framework import permissions, viewsets, mixins

from project.pagination import CustomPagination
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsProjectCreatorOrCollaborator, IsTaskRelatedToProject


class TaskViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectCreatorOrCollaborator, IsTaskRelatedToProject]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
