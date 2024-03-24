from rest_framework.routers import DefaultRouter
from task.views import TaskViewSet
from .views import ProjectViewSet

router = DefaultRouter()

router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'projects/(?P<project_id>[0-9]+)/tasks', TaskViewSet, basename='tasks')

urlpatterns = router.urls
