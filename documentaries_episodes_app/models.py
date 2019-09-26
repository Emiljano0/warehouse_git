from django.db import models
from datetime import datetime

class Documentaries_Episodes(models.Model):
    documentary_episode_id = models.IntegerField(primary_key=True, default=0)
    documentary_episode_documentaries_title = models.CharField(max_length=200, default='Planet Earth')
    documentary_episode_season = models.IntegerField(default=0)
    documentary_episode_number = models.IntegerField(default=0)
    documentary_episode_director = models.CharField(max_length=1000)
    documentary_episode_synopsis = models.CharField(max_length=1000)
    documentary_episode_title = models.CharField(max_length=100)
    documentary_episode_poster = models.FileField()
    documentary_episode_thumbnail = models.FileField(default='Planet Earth poster')
    documentary_episode_release_date = models.DateField(("Date"), default='0000')
    documentary_episode_budget = models.IntegerField()
    documentary_episode_gross = models.IntegerField()
    documentary_episode_genre = models.CharField(max_length=100, default='Action')
    documentary_episode_format = models.CharField(max_length=100)
    documentary_episode_rating = models.FloatField()
    documentary_episode_video = models.FileField(default='PlanetEarth.mp4')

    def __str__(self):
        return self.documentary_episode_documentaries_title + ' : ' + self.documentary_episode_title \
               + ' (s' + str(self.documentary_episode_season) + 'e' + str(self.documentary_episode_number) +')'