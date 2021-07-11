from django.contrib import admin

from .models import Game, Comment




@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'views', 'publish', 'slug')
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'game', 'likerate', 'publish')
    search_fields = ('author',)
