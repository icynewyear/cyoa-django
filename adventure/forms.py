from django import forms

from .models import Adventure, Room, Choice

class AdventureForm(forms.ModelForm):
    class Meta:
        model = Adventure
        fields = ('name','description',)

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('image','room_text','adventure',)

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('display_text','destination','associated_room',)
