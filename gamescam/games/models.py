from django.db import models
from django.contrib.auth.models import User # For the Game model author
from django.utils.text import slugify # For the game model slug

# Create your models here.
class Game(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    viewcount = models.IntegerField(default=0)
    state = models.CharField(max_length=5) # ok, nay, hold
    thumbnail = models.ImageField(null=True, blank=True, upload_to='gimgs/')
    pub_date = models.DateTimeField()
    slug = models.SlugField(max_length=30, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    state = models.CharField(max_length=5) # ok, nay, hold
    pub_date = models.DateTimeField()
    
    def __str__(self):
        return '{}: {}'.format(self.author, self.text)
    