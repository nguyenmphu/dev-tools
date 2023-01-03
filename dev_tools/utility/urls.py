from django.urls import path

from .views import md5

urlpatterns = [
    path("hash/md5", md5, name="md5"),
]
