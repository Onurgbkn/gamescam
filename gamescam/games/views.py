from django import template
from django.core import paginator
from django.http.response import HttpResponse, HttpResponseRedirect
from . models import Game
from django.shortcuts import get_object_or_404, render
from django.db.models import F # for the view count
import random # for the random game order
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Count

from . forms import CommentForm


# Create your views here.

def index(request):
    
    game_list = Game.objects.all()
    
    paginator = Paginator(game_list, 9)
    
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)
    
    context = {
        'game_list': page_obj,
    }
    
    return render(request, 'games/index.html', context)


def gameplay(request, slug):
    game = Game.objects.filter(slug=slug)
    
    game.update(viewcount=F('viewcount') + 1)
    
    game = game[0]

    game_tags_ids = game.tags.values_list('id', flat=True)
    similar_games = Game.objects.filter(tags__in=game_tags_ids).exclude(id=game.id)
    similar_games = similar_games.annotate(same_tags=Count('tags')).order_by('-same_tags','-created')[:8]
    
    context = {
        'game': game,
        'form': CommentForm(),
        'similar_games': similar_games,
    }

    return render(request, 'games/gameplay.html', context)


def comment(request, slug):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            game = get_object_or_404(Game, slug=slug)
            
            game.comment_set.create(author=form.cleaned_data['username'], text=form.cleaned_data['text'])
            
            messages.success(request, 'Comment submission successful')
            return HttpResponseRedirect(reverse('gameplay', args=(game.slug,)))



    
    