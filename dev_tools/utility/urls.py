from django.urls import path

from .views import md5

urlpatterns = [
    path("md5", md5, name="md5"),
]
