from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('successful')
    template_name = 'accounts/signup.html'


# TODO remove after figuring out where to actually redirect to after successful login/signup
class Successful(generic.TemplateView):
    template_name = 'accounts/successful_login.html'
