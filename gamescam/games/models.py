from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone



class Game(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # default=User.objects.get(username='lma10ur')
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=250)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    publish = models.DateTimeField()
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-publish',)

    def get_slug(self):
        return slugify(self.name)




class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    likerate = models.IntegerField(default=0)
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.author, self.text)

    class Meta:
        ordering = ('publish',)