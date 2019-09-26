from django.db import models
from datetime import datetime


class Series_Episodes(models.Model):
    series_episode_id = models.IntegerField(primary_key=True, default=0)
    series_episode_series_title = models.CharField(max_length=200, default='Planet Earth')
    series_episode_season = models.IntegerField(default=0)
    series_episode_number = models.IntegerField(default=0)
    series_episode_director = models.CharField(max_length=1000)
    series_episode_synopsis = models.CharField(max_length=1000)
    series_episode_title = models.CharField(max_length=100)
    series_episode_poster = models.FileField()
    series_episode_thumbnail = models.FileField(default='Planet Earth Thumbnail')
    series_episode_release_date = models.DateField(("Date"), default='0000')
    series_episode_budget = models.IntegerField()
    series_episode_gross = models.IntegerField()
    series_episode_genre = models.CharField(max_length=100, default='Action')
    series_episode_format = models.CharField(max_length=100)
    series_episode_rating = models.FloatField()
    series_episode_video = models.FileField(default='PlanetEarth.mp4')

    def __str__(self):
        return self.series_episode_series_title + ' : ' + self.series_episode_title \
               + ' (s' + str(self.series_episode_season) + 'e' + str(self.series_episode_number) + ')'
