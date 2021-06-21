from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView, UpdateView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


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
        thisslug = self.kwargs.get("slug")
        room = Room.startroom.filter(adventure__slug=thisslug).first()
        if room:
            context['start_room'] = room.pk
        return context

class AdventureListView(ListView):
    model = Adventure
    template_name = "adventure/adventure_list.html"
    context_object_name = 'adventure_list'

class AdventureCreateView(CreateView):
    model = Adventure
    template_name = "adventure/adventure_update.html"
    form_class = AdventureForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        return super().form_valid(form)

class AdventureUpdateView(UpdateView):
    model = Adventure
    template_name = "adventure/adventure_update.html"
    form_class = AdventureForm

class AdventurePlayView(DetailView):
    model = Adventure
    current_room = None
    template_name = "room/room_play.html"
    context_object_name = 'room'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

    def set_current_room():
        pass

    def get_first_room():
        query = Room.objects.filter(adventure__slug=thisslug).filter(start_room=True).first()
        room = get_object_or_404(query)
        return room

class RoomCreateView(CreateView):
    model = Room
    template_name = "adventure/adventure_update.html"
    form_class = AdventureForm

    def form_valid(self, form):
        slug = self.kwargs.get(self.slug_url_kwarg)
        queryset = Adventure.objects.filter(adventure__slug=slug).filter()
## TODO: finish this
        self.object = form.save(commit=False)
        self.object.adventure = self.request.user

        return super().form_valid(form)


class RoomPlayView(DetailView):
    model = Room
    template_name = "room/room_play.html"
    context_object_name = 'room'
    slug_url_kwarg = 'adv_slug'

    def get_object(self, queryset=None, **kwargs):
        slug = self.kwargs.get(self.slug_url_kwarg)
        r_pk = self.kwargs.get('pk')
        queryset = Room.objects.filter(adventure__slug=slug).filter(pk=r_pk)
        obj = super().get_object(queryset=queryset)
        return obj

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

def register_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('adventure-list')
    return render(request, 'user/register.html', {'form': form})
