from django.urls import path, include
from rest_framework import routers

from planetarium.views import (
    ShowThemeViewSet,
)

router = routers.DefaultRouter()
router.register(r'themes', ShowThemeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
