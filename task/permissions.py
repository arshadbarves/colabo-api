from rest_framework import permissions

class IsCollaboratorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.project.created_by == user or user in obj.project.collaborators.all()
