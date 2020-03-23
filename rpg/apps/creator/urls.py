from django.urls import path

from . import views

app_name = 'creator'
urlpatterns = [
    path('create/', views.CharacterCreateView.as_view(), name='create'),
    path('update/', views.CharacterUpdateView.as_view(), name='update'),
]
