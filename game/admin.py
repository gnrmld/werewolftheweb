from django.contrib import admin
from .models import Game, PlayersRoleInGame
# Register your models here.
admin.site.register(Game)
admin.site.register(PlayersRoleInGame)