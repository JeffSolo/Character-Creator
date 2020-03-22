from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import generic

from apps.creator.models import Characters


class HomeView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            return render(request, 'home.html')


class ProfileView(LoginRequiredMixin, generic.ListView):
    model = Characters
    template_name = 'rpg/profile.html'
    paginate_by = 10
    context_object_name = 'characters'

    def get_queryset(self):
        return Characters.objects.filter(user=self.request.user).order_by('name')
