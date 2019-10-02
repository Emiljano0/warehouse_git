from django.db import models
from datetime import datetime

class Documentaries_Episodes(models.Model):
    documentary_episode_title = models.CharField(max_length=100)
    documentary_episode_documentaries_title = models.CharField(max_length=200)
    documentary_episode_season = models.IntegerField(default=0)
    documentary_episode_number = models.IntegerField(default=0)
    documentary_episode_creator = models.CharField(max_length=1000)
    documentary_episode_description = models.CharField(max_length=1000)
    documentary_episode_release_date = models.DateField(("Date"), default='0000')
    documentary_episode_genre = models.CharField(max_length=100)
    documentary_episode_quality = models.CharField(max_length=100)
    documentary_episode_rating = models.FloatField()
    documentary_episode_poster = models.FileField()
    documentary_episode_thumbnail = models.FileField()
    documentary_episode_video = models.FileField()

    def __str__(self):
        return self.documentary_episode_documentaries_title + ' : ' + self.documentary_episode_title \
               + ' (s' + str(self.documentary_episode_season) + 'e' + str(self.documentary_episode_number) +')'
