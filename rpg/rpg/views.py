from django.views import generic


# TODO remove after figuring out where to actually redirect to after successful login/signup
class Home(generic.TemplateView):
    template_name = 'home.html'
