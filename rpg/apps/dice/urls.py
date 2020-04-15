from django.urls import path
from . import views


app_name = 'dice'
urlpatterns = [
    path('ajax/roll_stats/', views.rolled_stats, name='roll_stats'),
]
