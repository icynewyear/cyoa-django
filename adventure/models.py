from django.db import models
from django.urls import reverse
from Mixins.modelMixins import SlugModelMixin, SortableModelMixin

# Create your models here.

class Adventure(SlugModelMixin):
    name = models.CharField(blank=True, max_length=140)
    description = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("adventure-detail", kwargs={"pk": self.pk})

class Room(SortableModelMixin):
    ## TODO: handle upload path
    ## TODO: auto reordering


    image = models.ImageField(upload_to="dir/path/", null=True, blank=True)
    room_text = models.TextField(blank=True)
    ## TODO: add logic to make start_room True unique
    start_room = models.BooleanField(default=False)
    #Foreign Keys
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)

    group_by_field = 'adventure'

    def __str__(self):
        return self.room_text

    # def get_absolute_url(self):
    #     return reverse("room-detail", kwargs={"pk": self.pk})

class Choice(models.Model):
    display_text = models.CharField(blank=True, max_length=140)
    destination = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    #Foreign Key
    associated_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="choices")

    def __str__(self):
        output = self.associated_room.room_text[0:15]
        output += " | "
        output += self.display_text
        if self.destination:
            output += " > "
            output += self.destination.room_text[0:15]
        return output

    # def get_absolute_url(self):
    #     return reverse("choice-detail", kwargs={"pk": self.pk})
