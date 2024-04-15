from django.urls import path, include
from rest_framework import routers

from planetarium import views

router = routers.DefaultRouter()
router.register(r'themes', views.ShowThemeViewSet)
router.register(r'astronomy_shows', views.AstronomyShowViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
