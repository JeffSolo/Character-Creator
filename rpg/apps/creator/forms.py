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
    character_class = ClassModelChoiceField(queryset=Classes.objects.all(), empty_label=None)
    character_race = RaceModelChoiceField(queryset=Races.objects.all(), empty_label=None)
    level = forms.IntegerField(min_value=1, max_value=20, initial=1, disabled=True)
    abil_strength        = forms.IntegerField(label='STR', initial=8)
    abil_dexterity       = forms.IntegerField(label='DEX', initial=8)
    abil_constitution    = forms.IntegerField(label='CON', initial=8)
    abil_intelligence    = forms.IntegerField(label='INT', initial=8)
    abil_wisdom          = forms.IntegerField(label='WIS', initial=8)
    abil_charisma        = forms.IntegerField(label='CHA', initial=8)
    scores = forms.CharField(label='Ability Scores', initial="8, 10, 12, 13, 14, 15")

    class Meta:
        model = Characters
        exclude = ['user', 'character_info']
        widgets = {
            'scores': forms.TextInput(attrs={'readonly': 'True'})
        }
