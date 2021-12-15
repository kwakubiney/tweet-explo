from django.db import models

class Tweet(models.Model):
    tweet = models.CharField(max_length=280 , blank=False, default=None)
    date_created = models.DateTimeField()
    username = models.CharField(max_length=15, blank=False, default=None)

    def __str__(self):
        return self.tweet[0:10]
