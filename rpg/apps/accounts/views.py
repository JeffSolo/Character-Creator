from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # TODO redirect page
            return HttpResponseRedirect('')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/sign_up.html', {'form': form})


def login(request):
    pass


def logout(request):
    pass