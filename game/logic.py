from django.core.exceptions import ObjectDoesNotExist

from .models import Game, PlayersRoleInGame
from player.models import Player
from characters.models import Role
from random import shuffle


class GameInfo(object):
    is_host = False
    game_percent = 100
    turns_remaining = 100

    def __init__(self, request, game, visiting_ip):
        self.visiting_ip = visiting_ip
        self.get_game_info(request, game)

    def get_game_info(self,request, game):
        if game.host == self.visiting_ip:
            self.is_host = True

        role = Role.objects.get(pk=4)
        self.game_percent = 100 - (role.turn_order * 11.12)
        if self.game_percent < 0:
            self.turns_remaining = 0

        return self

def update_player_info(request, game, visiting_ip):
    player = Player.objects.get(pk=visiting_ip)
    player.last_played_game = game
    player.save()


def get_roles_in_game(request, game):
    if game.players_role_in_game.all().count() == 0:
        roles = Role.objects.all().order_by('character_priority')
        total_player = 0
        roles_in_game = []
        for role in roles:
            if total_player == game.max_players + 3:
                break
            for count in range(role.count):
                roles_in_game.append(role)
                total_player += 1
        shuffle(roles_in_game)
        for role_in_game in roles_in_game:
            players_role_in_game = PlayersRoleInGame()
            players_role_in_game.game = game
            players_role_in_game.role = role_in_game
            players_role_in_game.save()

    return game.players_role_in_game.all()


def get_player_role(request, game, visiting_ip):
    try:
        PlayersRoleInGame.objects.filter(game=game.pk).get(player=visiting_ip)
    except ObjectDoesNotExist:
        players_role_in_game_object = PlayersRoleInGame.objects.filter(game=game.pk).filter(player=None).first()
        player = Player.objects.get(pk=visiting_ip)
        players_role_in_game_object.player = player
        players_role_in_game_object.save()
    return PlayersRoleInGame.objects.filter(game=game.pk).get(player=visiting_ip).role


class GameFlow(object):
    def __init__(self, game):
        self.game = game
        if game.player.all().count() == game.max_players:
            game.start()
            self.turns()

    def turns():
        pass


