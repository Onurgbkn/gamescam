from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.content
    