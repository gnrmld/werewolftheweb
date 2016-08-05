from .models import Game
from player.models import Player
from characters.models import Role


class GameInfo(object):
    is_host = False
    game_percent = 100
    turns_remaining = 100

    def __init__(self,request, game):
        self.get_game_info(request, game)

    def get_game_info(self,request, game):
        visiting_ip = request.META.get('REMOTE_ADDR')
        if game.host == visiting_ip:
            self.is_host = True

        role = Role.objects.get(pk=4)
        self.game_percent = 100 - (role.turn_order * 11.12)
        if self.game_percent < 0:
            self.turns_remaining = 0

        return self

def update_player_info(request, game):
    visiting_ip = request.META.get('REMOTE_ADDR')
    player = Player.objects.get(pk=visiting_ip)
    player.last_played_game = game
    player.save()