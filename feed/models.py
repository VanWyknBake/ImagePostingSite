from django.db import models
from sorl.thumbnail import ImageField
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    #Title not in video!!!! Add everwhere!!!
    title = models.CharField(max_length=30, blank=False, null=False, default='')
    text = models.TextField(max_length=140, blank=False, null=False)
    image = models.ImageField(default='')
    date = models.DateTimeField(auto_now_add=True,
                                blank=True, null=True)

   

    def __str__(self):
        return self.title
        

