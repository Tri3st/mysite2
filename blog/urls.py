from django.urls import path

from info.urls import urlpatterns
from . import views


urlpatterns = [
    path("", views.index, name="index"),
]
