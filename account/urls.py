from rest_framework.routers import DefaultRouter
from .views import UserLoginViewSet, UserProfileViewSet, UserRegisterViewSet, UserLogoutViewSet

router = DefaultRouter()
router.register(r'signin', UserLoginViewSet, basename='user_signin')
router.register(r'signup', UserRegisterViewSet, basename='user_signup')
router.register(r'signout', UserLogoutViewSet, basename='user_signout')
router.register(r'profile', UserProfileViewSet, basename='user_profile')

urlpatterns = router.urls