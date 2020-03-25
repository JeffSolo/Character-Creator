from django import forms
from .models import Characters, Classes, Levels, Races


class ClassModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.class_name


class RaceModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.race


class LevelModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.level


class CharacterForm(forms.ModelForm):
    #user = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    character_class = ClassModelChoiceField(queryset=Classes.objects.all(), empty_label=None)
    character_race = RaceModelChoiceField(queryset=Races.objects.all(), empty_label=None)
    level = forms.IntegerField(min_value=1, max_value=20, initial=1, disabled=True)
    strength        = forms.IntegerField(label='STR', initial=10)
    dexterity       = forms.IntegerField(label='DEX', initial=10)
    constitution    = forms.IntegerField(label='CON', initial=10)
    intelligence    = forms.IntegerField(label='INT', initial=10)
    wisdom          = forms.IntegerField(label='WIS', initial=10)
    charisma        = forms.IntegerField(label='CHA', initial=10)
    class Meta:
        model = Characters
        exclude = ['user', 'character_info']
        widgets = {
            'user': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
