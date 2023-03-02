from django.urls import path, include

from .api.v1 import urls

urlpatterns = [
    path('', include(urls)),
]
