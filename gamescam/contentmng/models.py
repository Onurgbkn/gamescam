from django.db import models

# Create your models here.

class Game(models.Model):
    game_name = models.CharField(max_length=50)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.game_name


class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



    def __str__(self):
        return self.comment_text