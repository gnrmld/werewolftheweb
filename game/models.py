from django.db import models
from django.utils import timezone


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=20)
    host = models.CharField(max_length=20, blank=True, null=True)
    max_players = models.IntegerField(default=6)
    create_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def start(self):
        self.start_date = timezone.now()
        self.save()

    def end(self):
        self.end_date = timezone.now()
        self.save()

    def is_playable(self):
        return (self.create_date <= timezone.now() 
                        and self.start_date == None
                            and self.end_date == None)

    def __str__(self):
        return self.name

