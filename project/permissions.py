from rest_framework import permissions

class IsProjectCreatorOrCollaborator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.created_by == user or user in obj.collaborators.all()
