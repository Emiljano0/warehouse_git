from django.db import models
from datetime import datetime


class Series(models.Model):
    series_title = models.CharField(max_length=200)
    series_creator1 = models.CharField(max_length=100)
    series_creator2 = models.CharField(max_length=100)
    series_description = models.CharField(max_length=1000)
    series_release_date = models.DateField(("Date"), default='0000')
    series_genre = models.CharField(max_length=100)
    series_rating = models.FloatField()
    series_poster = models.FileField()

    def __str__(self):
        return self.series_title
