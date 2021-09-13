from django import template
from . models import Game
from django.shortcuts import render


# Create your views here.


def index(request):
    
    game_list = Game.objects.all()
    
    context = {
        'game_list': game_list,
    }
    
    return render(request, 'games/index.html', context)


def gameplay(request, slug):
    return render(request, 'games/gameplay.html', {})