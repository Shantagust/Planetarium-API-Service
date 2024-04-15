from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from planetarium import serializers
from planetarium.models import (
    ShowTheme,
    AstronomyShow,
    Reservation,

)


class ShowThemeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = ShowTheme.objects.all()
    serializer_class = serializers.ShowThemeSerializer


class AstronomyShowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = AstronomyShow.objects.all()
    serializer_class = serializers.AstronomyShowSerializer


class ReservationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer
