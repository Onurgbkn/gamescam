from django.db import models
from django.db.models.deletion import CASCADE



class Game(models.Model):
    game_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.game_name


class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text