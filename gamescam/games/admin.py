from django.contrib import admin

# Register your models here.
from .models import Game, Comment, Tag

admin.site.register(Comment)
admin.site.register(Tag)


class CommentInline(admin.TabularInline ):
    model = Comment
    extra = 1
    
    
    
class GameAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Game, GameAdmin)
