from django.http import HttpResponse
from django.template import loader
from .models import Game

# Create your views here.


def index(request):
    latest_game_list = Game.objects.order_by('-pub_date')[:5]
    template = loader.get_template('contentmng/index.html')
    context = {
        'latest_game_list': latest_game_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, game_id):
    return HttpResponse("You're in %s detail page." % game_id)
