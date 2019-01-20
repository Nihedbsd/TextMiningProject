from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=20)


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)