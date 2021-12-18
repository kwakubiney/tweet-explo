from rest_framework import serializers
from .models import Tweet
from django.conf import settings

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["id", "tweet", "username", "date_created"]
