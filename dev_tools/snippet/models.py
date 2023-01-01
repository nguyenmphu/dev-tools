from django.contrib.auth.models import User
from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=31)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return str(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=31)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return str(self.name)


class Snippet(models.Model):
    title = models.CharField(max_length=255)
    code = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
