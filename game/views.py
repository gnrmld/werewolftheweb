from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

from .models import Game
from .forms import GameForm
from .logic import GameInfo, update_player_info

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

    if is_not_signed_up(request):
        return redirect('player/create')

    game = get_object_or_404(Game, pk=pk)
    if game.player.count() >= game.max_players:
        messages.add_message(request, messages.ERROR, 'Game is Full.')
        return redirect(reverse('game_list'))

    players = game.player.all()

    game_info = GameInfo(request, game)
    print(game_info.is_host)
    update_player_info(request, game)
    context = {
        'game' : game,
        'players' : players,
        'game_info' : game_info,
    }
    
    return render(request, 'game/board.html', context)

def end_game(request, pk):
    game = Game.objects.get(pk=pk)
    game.end()
    return redirect('index')
