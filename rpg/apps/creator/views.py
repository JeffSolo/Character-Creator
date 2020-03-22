from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .forms import MainCharacterForm

from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from .models import Characters

class CharacterView(CreateView):
    model = Characters
    fields = ['user', 'character_class', 'character_race']
    exclude = 'Character info'
    template_name = 'creator/create_character.html'

class CharacterUpdate(UpdateView):
    model = Characters
    fields = '__all__'

class CharacterDelete(DeleteView):
    model = Characters

class MainView(FormView):
    form_class = MainCharacterForm
    template_name = 'creator/main.html'
    # success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
