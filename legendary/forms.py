from django import forms

from django.forms import ModelForm

from .models import Hero, Team, Mastermind, Scheme

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
                  'recruitment_points',
                  ]
        # fields = __all__
        # name = forms.CharField(label='Enter name', max_length=100)
        # team = forms.CharField(label='Enter team', max_length=50)
        # strenght = forms.IntegerField(label='strenght', max_value=14)
        # instinct = forms.IntegerField(label='instinct', max_value=14)
        # covert = forms.IntegerField(label='covert', max_value=14)
        # tech = forms.IntegerField(label='tech', max_value=14)
        # energy = forms.IntegerField(label='energy', max_value=14)


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