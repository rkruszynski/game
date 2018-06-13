from django.db import models
from django.core.validators import MaxValueValidator, validate_comma_separated_integer_list

# Create your models here.



class Team(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Hero(models.Model):

    RECRUITMENT_SCALE = (
        (0, 'None'),
        (1, 'A few'),
        (2, 'Medium'),
        (3, 'A lot of'),
    )

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    strenght = models.PositiveIntegerField()
    instinct = models.PositiveIntegerField()
    covert = models.PositiveIntegerField()
    tech = models.PositiveIntegerField()
    energy = models.PositiveIntegerField()
    piercing_energy = models.BooleanField(default=False)
    teleport = models.BooleanField(default=False)
    x_gene = models.BooleanField(default=False)
    versatile = models.BooleanField(default=False)
    recruitment_points = models.PositiveIntegerField(choices=RECRUITMENT_SCALE, default=0)

    def __str__(self):
        return self.name


class Mastermind(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Scheme(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


class Villians(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Henchmen(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):

    single_player = models.BooleanField(default=False)
    hero_1 = models.ForeignKey(Hero, on_delete=models.PROTECT, related_name='hero_1')
    hero_2 = models.ForeignKey(Hero, on_delete=models.PROTECT, related_name='hero_2')
    hero_3 = models.ForeignKey(Hero, on_delete=models.PROTECT, related_name='hero_3')
    hero_4 = models.ForeignKey(Hero, on_delete=models.PROTECT, related_name='hero_4', blank=True, null=True)
    hero_5 = models.ForeignKey(Hero, on_delete=models.PROTECT, related_name='hero_5', blank=True, null=True)
    mastermind = models.ForeignKey(Mastermind, on_delete=models.PROTECT)
    scheme = models.ForeignKey(Scheme, on_delete=models.PROTECT)
    win = models.BooleanField(default=True)
    comments = models.TextField(max_length=1000, blank=True)

