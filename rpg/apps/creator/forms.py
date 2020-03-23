from django import forms
from .models import Characters, Classes, Races


class ClassModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.class_name


class RaceModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.race

class CharacterForm(forms.ModelForm):
    #user = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    character_class = ClassModelChoiceField(queryset=Classes.objects.all())
    character_race = RaceModelChoiceField(queryset=Races.objects.all())
    class Meta:
        model = Characters
        exclude = ['user', 'character_info']
