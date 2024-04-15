from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from planetarium.models import ShowTheme


def index(request):
    return HttpResponse("Hello, world. You're at the planetarium index.")


class ShowThemeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = ShowTheme.objects.all()
    serializer_class = None
