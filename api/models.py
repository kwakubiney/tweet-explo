from django.db import models

class Tweet(models.Model):
    tweet = models.CharField(max_length=280 , blank=False, default=None)
    date_created = models.DateTimeField()
    time_created = models.TimeField()
    username = models.CharField(max_length=15, blank=False, default=None)

