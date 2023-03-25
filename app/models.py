from django.db import models


class students(models.Model):
    name = models.CharField(max_length=500)
    age = models.CharField(max_length=500)
    city = models.CharField(max_length=300, blank=True)
