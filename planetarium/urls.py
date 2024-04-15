from django.urls import path

from planetarium import views

urlpatterns = [
    path('', views.index, name='index'),
]
