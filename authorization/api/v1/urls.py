from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import PasswordViewSet

urlpatterns = [
    path('v1/auth/login/', TokenObtainPairView.as_view(),
         name='authorization_login'),
    path('v1/auth/refresh/', TokenRefreshView.as_view(),
         name='authorization_refresh'),
    path('v1/auth/password/', PasswordViewSet.as_view(),
         name='authorization_password'),
    path('v1/auth/password-reset/', include('django_rest_passwordreset.urls',
         namespace='authorization_password_reset')),
]
