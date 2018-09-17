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
    soaring_flight = models.BooleanField(default=False)
    lightshow = models.BooleanField(default=False)
    berserk = models.BooleanField(default=False)
    split_cards = models.BooleanField(default=False)
    recruitment_points = models.PositiveIntegerField(choices=RECRUITMENT_SCALE, default=0)
    costs = models.PositiveIntegerField(default=0)

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


class Villain(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Henchman(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):

    LUCK_SCALE = (
        (None, 'Can\'t be set'),
        (1, 'Very bad luck'),
        (2, 'Should be better'),
        (3, 'Just ok'),
        (4, 'It was lucky'),
        (5, 'We had a lot of luck!'),
    )

    CLOSE_TO_WIN_SCALE = (
        (0, 'Can\'t be set'),
        (1, 'Not even started!'),
        (2, 'Just in dreams'),
        (3, 'Had some hope, but not so close'),
        (4, 'More luck and probably winning'),
        (5, 'Almost! Almost winning!'),
        (6, 'Win!'),
    )

    NUMBER_OF_PLAYERS = (
        (1, 'Solo game'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
        (6, 'Six'),
    )

    def default_players(self):
        if self.single_player:
            return 1
        else:
            return 2

    single_player = models.BooleanField(default=False)
    number_of_players = models.PositiveIntegerField(choices=NUMBER_OF_PLAYERS, blank=True, null=True)
    hero_1 = models.ForeignKey(Hero, on_delete=models.PROTECT, related_name='hero_1')
    hero_2 = models.ForeignKey(Hero, on_delete=models.PROTECT, related_name='hero_2')
    hero_3 = models.ForeignKey(Hero, on_delete=models.PROTECT, related_name='hero_3')
    hero_4 = models.ForeignKey(Hero, on_delete=models.PROTECT, related_name='hero_4', blank=True, null=True)
    hero_5 = models.ForeignKey(Hero, on_delete=models.PROTECT, related_name='hero_5', blank=True, null=True)
    mastermind = models.ForeignKey(Mastermind, on_delete=models.PROTECT)
    villains_1 = models.ForeignKey(Villain, on_delete=models.PROTECT, related_name='villains_1')
    villains_2 = models.ForeignKey(Villain, on_delete=models.PROTECT, related_name='villains_2', blank=True, null=True)
    villains_3 = models.ForeignKey(Villain, on_delete=models.PROTECT, related_name='villains_3', blank=True, null=True)
    villains_4 = models.ForeignKey(Villain, on_delete=models.PROTECT, related_name='villains_4', blank=True, null=True)
    henchman_1 = models.ForeignKey(Henchman, on_delete=models.PROTECT, related_name='henchman_1')
    henchman_2 = models.ForeignKey(Henchman, on_delete=models.PROTECT, related_name='henchman_2', blank=True, null=True)
    scheme = models.ForeignKey(Scheme, on_delete=models.PROTECT)
    win = models.BooleanField(default=True)
    luck = models.PositiveIntegerField(choices=LUCK_SCALE, default=None, blank=True, null=True)
    difficulty = models.IntegerField(choices=CLOSE_TO_WIN_SCALE, default=None, blank=True, null=True)
    comments = models.TextField(max_length=1000, blank=True)

    def save(self, *args, **kwargs):
        if not self.number_of_players:
            self.number_of_players = self.default_players()
        super(Game, self).save(*args, **kwargs)

