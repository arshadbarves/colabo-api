from rest_framework.routers import DefaultRouter
from .views import UserLoginViewSet, UserRegisterViewSet, UserLogoutViewSet

router = DefaultRouter()
router.register(r'login', UserLoginViewSet, basename='user_login')
router.register(r'register', UserRegisterViewSet, basename='user_register')
router.register(r'logout', UserLogoutViewSet, basename='user_logout')

urlpatterns = router.urls