from django.db import models
from taggit.managers import TaggableManager
import time

class Album(models.Model):
  artist = models.CharField(max_length=200)
  album = models.CharField(max_length=500)
  year = models.PositiveSmallIntegerField(default=0)
  date_added = models.DateField('date added', null=True)
  date_listened = models.DateField('date listened', null=True, blank=True)
  listened = models.BooleanField(default=False)
  in_progress = models.BooleanField(default=False)
  score = models.PositiveSmallIntegerField(default=0)
  notes = models.TextField(default="", blank=True)
  tags = TaggableManager()

  def __str__(self):
    return self.artist + " - " + self.album + " (" + str(self.year) + ")"