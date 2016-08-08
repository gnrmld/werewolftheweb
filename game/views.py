from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

from .models import Game, PlayersRoleInGame
from .forms import GameForm
from .logic import GameInfo, GameFlow, \
    update_player_info, get_roles_in_game, get_player_role

from characters.models import Role
from player.models import Player

from player.views import is_not_signed_up

def index(request):
    '''Host or Join existing game'''
    if is_not_signed_up(request):
        return redirect('player/create')
    context = {}
    return render(request, 'game/index.html', context)

def create(request):
    '''Create your own game'''
    if is_not_signed_up(request):
        return redirect('player/create')
    
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.host = request.META.get('REMOTE_ADDR')
            if game.max_players < 6:
                game.max_players = 6
            elif game.max_players >16:
                game.max_players = 16
            game.save()
            return redirect('board', pk = game.pk)
    else:
        form = GameForm()

    context = {
        'form' : form,
    }
    return render(request, 'game/create.html', context)

def game_list(request):
    '''Shows all playable games
    (not started and not closed)'''
    if is_not_signed_up(request):
        return redirect('player/create')

    game_list = Game.objects.all()
    games = [game for game in game_list if game.is_playable()]
    context = {
        'games' : games,
    }
    return render(request, 'game/list.html', context)


def board(request, pk):
    '''The 'board' where players
    play werewolf one night'''
    visiting_ip = request.META.get('REMOTE_ADDR')
    if is_not_signed_up(request):
        return redirect('player/create')

    player_info = Player.objects.get(pk=visiting_ip)

    game = get_object_or_404(Game, pk=pk)
    if player_info.last_played_game != game and game.player.count() >= game.max_players:
        messages.add_message(request, messages.ERROR, 'Game is Full.')
        return redirect(reverse('game_list'))

    players = game.player.all().exclude(pk=visiting_ip)

    game_info = GameInfo(request, game, visiting_ip)
    update_player_info(request, game, visiting_ip)

    roles_in_game = get_roles_in_game(request, game)
    center_cards = roles_in_game.reverse()[:3]

    role = get_player_role(request, game, visiting_ip)

    print(GameFlow(game))

    context = {
        'game' : game,
        'players' : players,
        'game_info' : game_info,
        'role': role,
        'center_cards' : center_cards,
    }

    return render(request, 'game/board.html', context)



def end_game(request, pk):
    game = Game.objects.get(pk=pk)
    game.end()
    return redirect('index')
