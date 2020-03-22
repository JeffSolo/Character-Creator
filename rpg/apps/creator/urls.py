from django.urls import path

from . import views

app_name = 'creator'
urlpatterns = [
    path('main/', views.MainView.as_view(), name='main_character'),
    path('create/', views.CharacterView.as_view(), name='create'),
    path('update/', views.CharacterUpdate.as_view(), name='create'),
]
