from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path, reverse
from django.views.generic.base import RedirectView
from .views import SignUp

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/success/', RedirectView.as_view(pattern_name='characters'), name='login_success'),
]
