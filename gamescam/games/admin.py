from django.contrib import admin

# Register your models here.
from .models import Game, Comment, Tag

admin.site.register(Game)
admin.site.register(Comment)
admin.site.register(Tag)
