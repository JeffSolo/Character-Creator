from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic
from apps.creator.models import Characters


# TODO remove after figuring out where to actually redirect to after successful login/signup
class HomeView(generic.TemplateView):
    template_name = 'home.html'


class ProfileView(LoginRequiredMixin, generic.ListView):
    model = Characters
    template_name = 'rpg/profile.html'
    paginate_by = 10
    context_object_name = 'characters'

    def get_queryset(self):
        return Characters.objects.filter(user=self.request.user).order_by('name')
