from django import template
from . models import Game
from django.shortcuts import render
from django.db.models import F # for the view count


# Create your views here.


def index(request):
    
    game_list = Game.objects.all()
    
    context = {
        'game_list': game_list,
    }
    
    return render(request, 'games/index.html', context)


def gameplay(request, slug):
    game = Game.objects.filter(slug=slug)
    
    game.update(viewcount=F('viewcount') + 1)
    
    game = game[0]

    
    similar_games = Game.objects.exclude(id=game.id)
    context = {
        'game': game,
        'similar_games': similar_games,
    }

    return render(request, 'games/gameplay.html', context)