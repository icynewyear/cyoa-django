from django.db import models
from Mixins.modelMixins import SlugModelMixin

# Create your models here.
class Adventure(SlugModelMixin):
    name = models.CharField(blank=True, max_length=140)
    description = models.CharField(blank=True, max_length=255)

class Room(models.Model):
    ## TODO: handle upload path
    ## TODO: auto reordering
    image = models.ImageField(upload_to="/dir/path")
    room_text = models.TextField(blank=True)
    #Foreign Keys
    adventure = models.ForeignKey(Adventure, on_delete=model.CASCADE)

class Choice(models.Model):
    display_text = models.CharField(blank=True, max_length=140)
    destination = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    #Foreign Key
    room = models.ForeignKey(Room, on_delete=model.CASCADE)
