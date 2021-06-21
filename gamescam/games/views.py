from django import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Game
from django.template import loader


def index(request):
    latest_games = Game.objects.order_by('-pub_date')[:5]
    template = loader.get_template('games/index.html')
    context = {
        'latest_games': latest_games,
    }
    return HttpResponse(template.render(context, request))


def detail(request, game_id):
    return HttpResponse("Detail page of %s" % game_id)