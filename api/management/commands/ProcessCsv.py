from django.core.management.base import BaseCommand
from django.conf import settings
from api.models import Tweet
import csv


class Command(BaseCommand):
    def handle(self, *args , **options):
        with open(f"{settings.BASE_DIR}/csv/tweets.csv") as f:
            csv_reader = csv.reader(f , delimiter=",")
            next(csv_reader)
            for index, row in enumerate(csv_reader):
                Tweet.objects.create(tweet = row[1], date_created = row[5], username=row[11])
                if index > 99:
                    break
                    
            