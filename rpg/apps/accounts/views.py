from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # TODO redirect to better place
            return HttpResponseRedirect(reverse('accounts'))
    else:
        form = UserCreationForm()

    return render(request, 'accounts/sign_up.html', {'form': form})

# TODO remove after figuring out where to actually redirect to after successful login/signup
def login_successful(request):
    return HttpResponse('Success')

def login(request):
    pass

def logout(request):
    pass