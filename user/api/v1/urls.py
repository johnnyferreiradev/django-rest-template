from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

route = routers.DefaultRouter()

route.register(r'v1/user', UserViewSet, basename='User')


urlpatterns = [path('', include(route.urls))]
