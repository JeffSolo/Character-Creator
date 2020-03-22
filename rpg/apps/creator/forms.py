from django.forms import Form, ModelForm
from .models import Classes, Races, Characters


class MainCharacterForm(ModelForm):
    class Meta:
        model = Characters
        exclude = ['character_info']
    # player_name = forms.CharField(label='Player Name', max_length=32)
    # character_name = forms.CharField(label='Character Name', max_length=32)
    #race = forms.ModelChoiceField(queryset=Races.race_type.all())
    #classes = forms.ModelChoiceField(queryset=Classes.class_name.all())
