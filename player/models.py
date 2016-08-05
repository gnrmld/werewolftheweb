from django.db import models
from game.models import Game


# Create your models here.
class Player(models.Model):
    ip = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.CharField(max_length=20)
    last_played_game = models.ForeignKey(Game, related_name='player', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
