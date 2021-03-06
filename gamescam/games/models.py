from django.db import models
from django.contrib.auth.models import User # For the Game model author
from django.utils.text import slugify # For the game model slug
# IMAGE COMPRESS ============
from PIL import Image
from io import BytesIO
from django.core.files import File
# IMAGE COMPRESS ============
from django.utils.timesince import timesince


STATES = (
    ('ok', 'ok'),
    ('nay', 'nay'),
    ('hold', 'hold'),    
)


# Create your models here.
class Game(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    viewcount = models.IntegerField(default=0)
    state = models.CharField(max_length=5, choices=STATES) # ok, nay, hold
    thumbnail = models.ImageField(upload_to='gimgs/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    tags = models.ManyToManyField('Tag')
    
    def save(self, *args, **kwargs):
        

        if not self.slug or (self.slug not in self.thumbnail.name):
            new_image = self.compressimage(self.thumbnail)
            self.thumbnail = new_image
        
        self.slug = slugify(self.name) # add slug
        
        
        super(Game, self).save(*args, **kwargs)
        
    
    def __str__(self):
        return self.name
    
    
    def compressimage(self, oldImage):
        img = Image.open(oldImage)
        img = img.convert('RGB')
        imo = BytesIO()
        img.save(imo, 'JPEG', quality=70, optimize=True)
        newImage = File(imo, name=slugify(self.name) + '.jpg')
        return newImage
    
    def age(self):
        return timesince(self.created).split(', ')[0]
    
    def likerate(self):
        if self.likes + self.dislikes == 0:
            return 50
        else:
            return int(self.likes/(self.likes + self.dislikes) * 100)
        
    
    
    


class Comment(models.Model):
    
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    state = models.CharField(max_length=5, choices=STATES, default='hold') # ok, nay, hold
    created = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return '{}: {}'.format(self.author, self.text)
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def age(self):
        return timesince(self.created).split(', ')[0]
    