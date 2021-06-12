from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView, UpdateView

from .models import Adventure, Room, Choice
from .forms import AdventureForm, RoomForm, ChoiceForm
# Create your views here.

class AdventureDetailView(DetailView):
    model = Adventure
    template_name = "adventure/adventure_detail.html"
    context_object_name = 'adventure'

    #adds start_room to context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thisid = self.kwargs.get("pk")
        room = Room.objects.filter(adventure=thisid).filter(start_room=True)
        if(room.count() > 0):
            context['start_room'] = room
        return context

class AdventureListView(ListView):
    model = Adventure
    template_name = "adventure/adventure_list.html"
    context_object_name = 'adventure_list'

class AdventureCreateView(CreateView):
    model = Adventure
    template_name = "adventure/adventure_update.html"
    form_class = AdventureForm

class AdventureUpdateView(UpdateView):
    model = Adventure
    template_name = "adventure/adventure_update.html"
    form_class = AdventureForm

class RoomDetailView(DetailView):
    model = Room
    template_name = "room/room_detail.html"
    context_object_name = 'room'

class RoomListView(ListView):
    model = Adventure
    template_name = "room/room_list.html"
    context_object_name = 'room_list'

class RoomCreateView(CreateView):
    model = Room
    template_name = "room/room_update.html"
    form_class = RoomForm

class RoomUpdateView(UpdateView):
    model = Room
    template_name = "room/room_update.html"
    form_class = RoomForm
