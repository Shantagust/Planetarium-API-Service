from django.urls import path, include
from rest_framework import routers

from planetarium import views

router = routers.DefaultRouter()
router.register(r'themes', views.ShowThemeViewSet)
router.register(r'astronomy_shows', views.AstronomyShowViewSet)
router.register(r'reservations', views.ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
