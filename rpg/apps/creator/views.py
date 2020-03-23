from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .forms import CharacterForm
from .models import Characters


class CharacterCreateView(CreateView):
    form_class = CharacterForm
    template_name = 'creator/create.html'
    context_object_name = 'char_list'

    def get_initial(self):
        initial = super(CharacterCreateView, self).get_initial()
        initial.update({
            'level': 1,
        })
        if self.request.user.is_authenticated:
            initial.update({
                'user': self.request.user,
                'name': self.request.user.username,
            })
        return initial

    def form_valid(self, form):
        #form.instance.user = self.request.user
        return super().form_valid(form)


class CharacterUpdateView(UpdateView):
    form_class = CharacterForm


class CharacterDeleteView(DeleteView):
    form_class = CharacterForm
