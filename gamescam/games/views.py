from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Comment, Game
from django.template import loader

from .forms import CommentForm


def index(request):
    latest_games = Game.objects.order_by('-pub_date')[:5]
    context = {
        'latest_games': latest_games,
    }
    return render(request, 'games/index.html', context)


def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'games/detail.html', {'game': game})


def comment(request, game_id):

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            Game.objects.get(pk=game_id).comment_set.create(comment_text = form.cleaned_data['comment'])

    return HttpResponse('thanks')