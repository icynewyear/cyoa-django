from django import forms
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from .models import Adventure, Room, Choice

class AdventureForm(forms.ModelForm):
    class Meta:
        model = Adventure
        fields = ('name','description',)

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['slug'] = slugify(cleaned_data['name'])
        return cleaned_data

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('image','room_text','adventure',)

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('display_text','destination','associated_room',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
