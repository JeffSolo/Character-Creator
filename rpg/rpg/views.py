from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import generic

from apps.creator.models import Characters


class HomeView(generic.TemplateView):
    template_name = 'rpg/home.html'


class CharactersView(LoginRequiredMixin, generic.ListView):
    model = Characters
    template_name = 'rpg/characters.html'
    paginate_by = 10
    context_object_name = 'characters'

    def get_queryset(self):
        return Characters.objects.filter(user=self.request.user).order_by('name')
