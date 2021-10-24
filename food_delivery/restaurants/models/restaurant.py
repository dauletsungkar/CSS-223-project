from django.db import models


class Restaurant(models.Model):
    title = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
