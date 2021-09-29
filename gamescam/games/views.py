from django import template
from django.http.response import HttpResponse, HttpResponseRedirect
from . models import Game
from django.shortcuts import get_object_or_404, render
from django.db.models import F # for the view count
import random # for the random game order
from django.urls import reverse


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
        'similar_games': random.sample(list(similar_games), 8),
    }

    return render(request, 'games/gameplay.html', context)

def comment(request, slug):
    game = get_object_or_404(Game, slug=slug)
    
    game.comment_set.create(author=request.POST['username'], text=request.POST['comment'])
    return HttpResponseRedirect(reverse('gameplay', args=(game.slug,)))