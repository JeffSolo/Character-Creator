from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)

        return redirect('profile')
