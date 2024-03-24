from rest_framework import permissions


class IsProjectCreatorOrCollaborator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.project.created_by == user or user in obj.project.collaborators.all()


class IsTaskRelatedToProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.project.id == int(view.kwargs['project_id'])
