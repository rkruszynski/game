from django import forms

from django.forms import ModelForm

from .models import Hero, Team, Mastermind, Scheme, Game, Henchman, Villain

class HeroForm(ModelForm):
    class Meta:
        model = Hero
        fields = '__all__'
        fields = ['name',
                  'team',
                  'strenght',
                  'instinct',
                  'covert',
                  'tech',
                  'energy',
                  'piercing_energy',
                  'teleport',
                  'x_gene',
                  'versatile',
                  'soaring_flight',
                  'lightshow',
                  'berserk',
                  'split_cards',
                  'recruitment_points',
                  'costs',
                  ]


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class MastermindForm(ModelForm):
    class Meta:
        model = Mastermind
        fields = '__all__'


class SchemeForm(ModelForm):
    class Meta:
        model = Scheme
        fields = '__all__'


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class VillainForm(ModelForm):
    class Meta:
        model = Villain
        fields = '__all__'


class HenchmanForm(ModelForm):
    class Meta:
        model = Henchman
        fields = '__all__'


class SelectHeroForm(forms.Form):
    field = forms.IntegerField(max_value=50)
