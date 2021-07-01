from django import template
from django.core import paginator
from django.shortcuts import render, get_object_or_404, resolve_url
from django.http import HttpResponse, HttpResponseRedirect
from .models import Comment, Game
from django.template import loader
from django.core.paginator import Page, Paginator, EmptyPage, PageNotAnInteger

from .forms import CommentForm


def index(request):
    latest_games = Game.objects.order_by('-publish')
    paginator = Paginator(latest_games, 1)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    try:
        game_list = paginator.page(page_number)
    except PageNotAnInteger:
        game_list = paginator.page(1)

    context = {
        'latest_games': game_list,
        'page_obj': page_obj,
    }
    return render(request, 'games/index.html', context)


def detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'games/detail.html', {'game': game})


def comment(request, game_id):

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            Game.objects.get(pk=game_id).comment_set.create(comment_text = form.cleaned_data['comment'])

    return HttpResponse('thanks')