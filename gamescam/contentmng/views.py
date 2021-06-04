from django.http import HttpResponse
from django.http.response import Http404
from .models import Game
from django.shortcuts import render, get_object_or_404

# Create your views here.


    
def index(request):
    latest_game_list = Game.objects.order_by('-pub_date')[:5]
    context = {'latest_game_list': latest_game_list}
    return render(request, 'contentmng/index.html', context)



def detail(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("The game you looking for is not here.")
    return render(request, 'contentmng/detail.html', {'game': game})

    
def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'contentmng/detail.html', {'game': game})
