from django.db import models

class Event(models.Model):
  id = models.IntegerField(primary_key=True)
  title = models.CharField(max_length=128)
  address = models.CharField(max_length=128, null=True, blank=True)
  place = models.CharField(max_length=128, null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  event_url = models.URLField(null=True, blank=True)
  started_at = models.DateTimeField(null=True, blank=True)
  ended_at = models.DateTimeField(null=True, blank=True)
  limit = models.IntegerField(null=True, blank=True)
  accepted = models.IntegerField(null=True, blank=True)
  waiting = models.IntegerField(null=True, blank=True)
  lat = models.FloatField(null=True, blank=True)
  lon = models.FloatField(null=True, blank=True)
