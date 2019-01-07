from django.shortcuts import render, get_object_or_404

from .models import Hero, Team, Mastermind, Scheme, Game, Villain, Henchman
from django.http import Http404, HttpResponseRedirect
from .forms import HeroForm, TeamForm, MastermindForm, SchemeForm, GameForm, VillainForm, HenchmanForm
from django.contrib import messages
from django.db.models import Q
from collections import Counter
from .utils import skills_combined
from .settings import SHOW_BEST_TEAM_BY_NAME
import operator
import time


# Create your views here.


def index(request):

    heros = Hero.objects.all()
    context = {}
    for hero in heros:
        games = Game.objects.filter(Q(hero_1=hero.id) | Q(hero_2=hero.id) | Q(hero_3=hero.id) | Q(hero_4=hero.id) | Q(hero_5=hero.id))
        context[hero] = len(games)

    return render(request, 'legendary/index.html', {'heros': context})


def hero_detail(request, hero_id):
    try:
        hero = Hero.objects.get(pk=hero_id)
    except Hero.DoesNotExist:
        raise Http404("Hero does not exist!")

    all_games = len(Game.objects.all())

    games = Game.objects.filter(
        Q(hero_1=hero.id) | Q(hero_2=hero.id) | Q(hero_3=hero.id) | Q(hero_4=hero.id) | Q(hero_5=hero.id))
    games_win = 0
    other_heroes = []
    for game in games:
        tmp_id_list = [game.hero_1.id, game.hero_2.id, game.hero_3.id]
        try:
            tmp_id_list.append(game.hero_4.id)
        except:
            pass
        try:
            tmp_id_list.append(game.hero_5.id)
        except:
            pass
        tmp_id_list = list(set(tmp_id_list))
        tmp_id_list.remove(hero_id)  # remove player himself
        other_heroes.append(tmp_id_list)
        if game.win:
            games_win += 1

    win_percentage = "{0:.2f}".format(games_win/len(games)*100) if games else 0
    cnt = Counter([x for y in other_heroes for x in y])
    result = [e for e in cnt if cnt[e] == cnt.most_common()[0][1]]
    hero_names = [Hero.objects.get(pk=x).name for x in result]
    try:
        most_games = cnt.most_common()[0][1]
    except:
        most_games = 0

    stats = {
        'all_games': all_games,
        'hero_games': len(games),
        'games_win': games_win,
        'win_percentage': win_percentage,
        'most_games': most_games,
        'other_heroes': hero_names,
    }

    return render(request, 'legendary/hero_detail.html', {'hero': hero,
                                                          'stats': stats,
                                                          'games': games},
                  )


def hero_delete(request, hero_id):
    obj = get_object_or_404(Hero, pk=hero_id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "This hero was succesfully deleted")
        return HttpResponseRedirect('/legendary/')
    context = {
        "object": obj
    }
    return render(request, "legendary/confirm_delete.html", context)


def team_detail(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        raise Http404("Team does not exist!")
    heros = Hero.objects.filter(team=team_id)
    return render(request, 'legendary/team_detail.html', {'team': team, 'heros': heros})


def create(request):
    if request.method == 'POST':
        hero_form = HeroForm(request.POST)
        hero_form.save()
        return HttpResponseRedirect('/legendary/thanks/')
    else:
        form = HeroForm()
    return render(request, 'legendary/create.html', {'form': form})


def add_team(request):
    if request.method == 'POST':
        team_form = TeamForm(request.POST)
        team_form.save()
        return HttpResponseRedirect('/legendary/teams')
    else:
        team_form = TeamForm()
    return render(request, 'legendary/add_team.html', {'form': team_form})


def teams_page(request):
    teams = Team.objects.all()
    context = {}

    for team in teams:
        counter = len(Hero.objects.filter(team=team.id))
        context[team] = counter
    return render(request, 'legendary/teams.html', {'teams': context})


def thanks(request):
    return render(request, 'legendary/thanks.html')


def masterminds_page(request):
    masterminds = Mastermind.objects.order_by('name')
    return render(request, 'legendary/masterminds.html', {'masterminds': masterminds})


def add_mastermind(request):
    if request.method == 'POST':
        mastermind_form = MastermindForm(request.POST)
        messages.success(request, ('Thank you'))
        mastermind_form.save()
        return HttpResponseRedirect('masterminds')
    else:
        mastermind_form = MastermindForm()
    return render(request, 'legendary/add_mastermind.html', {'form':mastermind_form})


def add_scheme(request):
    if request.method == "POST":
        scheme_form = SchemeForm(request.POST)
        scheme_form.save()
        # schemes = Scheme.objects.order_by('name')
        return HttpResponseRedirect('schemes')
    else:
        scheme_form = SchemeForm()
    return render(request, 'legendary/add_scheme.html', {'form':scheme_form})


def schemes_page(request):
    schemes = Scheme.objects.order_by('name')
    return render(request, 'legendary/schemes.html', {'schemes': schemes})


def add_game(request):
    if request.method == "POST":
        game_form = GameForm(request.POST)
        game_form.save()
        return HttpResponseRedirect('/legendary/games')
    else:
        game_form = GameForm()
    return render(request, 'legendary/add_game.html', {'form': game_form})


def games_page(request):
    games = Game.objects.all()
    return render(request, 'legendary/games_page.html', {'games': games})


def villains(request):
    villains = Villain.objects.all()
    return render(request, 'legendary/villains_page.html', {'villains': villains})


def add_villain(request):
    if request.method == "POST":
        villain_form = VillainForm(request.POST)
        villain_form.save()
        return HttpResponseRedirect('/legendary/villains')
    else:
        villain_form = VillainForm()
    return render(request, 'legendary/add_villain.html', {'form':villain_form})


def delete_villain(request, villain_id):
    obj = get_object_or_404(Villain, pk=villain_id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "This Villain was succesfully deleted")
        return HttpResponseRedirect('/legendary/villains')
    context = {
        "object": obj
    }
    return render(request, "legendary/confirm_delete.html", context)


def henchman(request):
    henchman = Henchman.objects.all()
    return render(request, 'legendary/henchman_page.html', {'henchmen': henchman})


def add_henchman(request):
    if request.method == "POST":
        henchman_form = HenchmanForm(request.POST)
        henchman_form.save()
        return HttpResponseRedirect('/legendary/henchmen')
    else:
        henchman_form = VillainForm()
    return render(request, 'legendary/add_villain.html', {'form': henchman_form})

def hero_best_team(request, hero_id):

    heros_attributes = {}
    heros = Hero.objects.all()
    for hero in heros:
        if SHOW_BEST_TEAM_BY_NAME:
            heros_attributes[hero.name] = [hero.strenght, hero.instinct, hero.covert, hero.tech, hero.energy]
            current_hero = Hero.objects.get(pk=hero_id).name
        else:
            heros_attributes[hero.id] = [hero.strenght, hero.instinct, hero.covert, hero.tech, hero.energy]
            current_hero = hero_id


    all_teams = skills_combined(heros_attributes, current_hero)
    stats = {}
    with open ('newfile.txt', 'w') as newfile:
        for i in range(len(all_teams[:500])):
            hero1 = Hero.objects.get(pk=all_teams[i][1][0])
            hero2 = Hero.objects.get(pk=all_teams[i][1][1])
            hero3 = Hero.objects.get(pk=all_teams[i][1][2])
            stats[i] = {'value': all_teams[i][0],
                        'hero1': hero1.name,
                        'hero2': hero2.name,
                        'hero3': hero3.name,
                        'strenght': sum([hero1.strenght, hero2.strenght, hero3.strenght]),
                        'instinct': sum([hero1.instinct, hero2.instinct, hero3.instinct]),
                        'covert': sum([hero1.covert, hero2.covert, hero3.covert]),
                        'tech': sum([hero1.tech, hero2.tech, hero3.tech]),
                        'energy': sum([hero1.energy, hero2.energy, hero3.energy]),
                        'piercing_energy': sum([hero1.piercing_energy, hero2.piercing_energy, hero3.piercing_energy]),
                        'teleport': sum([hero1.teleport, hero2.teleport, hero3.teleport]),
                        'x_gene': sum([hero1.x_gene, hero2.x_gene, hero3.x_gene]),
                        'versatile': sum([hero1.versatile, hero2.versatile, hero3.versatile]),
                        'soaring_flight': sum([hero1.soaring_flight, hero2.soaring_flight, hero3.soaring_flight]),
                        'lightshow': sum([hero1.lightshow, hero2.lightshow, hero3.lightshow]),
                        'berserk': sum([hero1.berserk, hero2.berserk, hero3.berserk]),
                        'split_cards': sum([hero1.split_cards, hero2.split_cards, hero3.split_cards]),

                        }


            newfile.write(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
            newfile.write('\n')


    return render(request, 'legendary/hero_best_team.html', {'heros': stats})


def statistics(request):
    games = Game.objects.all()
    games_won = len([x for x in games if x.win])
    solo_games = [x for x in games if x.single_player]
    solo_games_win = len([x for x in solo_games if x.win])
    non_solo_games = [x for x in games if not x.single_player]
    non_solo_games_win = len([x for x in non_solo_games if x.win])
    games_won_percentege = "{0:.2f}".format(games_won/len(games)*100) if games else 0
    solo_games_percentege = "{0:.2f}".format(len(solo_games) / len(games) * 100) if solo_games else 0
    non_solo_games_win_percentage = "{0:.2f}".format(non_solo_games_win/len(non_solo_games)*100) if non_solo_games else 0
    heros_played = []
    heros_all = Hero.objects.all()
    for game in games:
        heros_played.append(game.hero_1)
        heros_played.append(game.hero_2)
        heros_played.append(game.hero_3)
        if game.hero_4:
            heros_played.append(game.hero_4)
        if game.hero_5:
            heros_played.append(game.hero_5)
    most_played_heros = set([hero.name for hero in heros_played if heros_played.count(hero) == Counter(heros_played).most_common()[0][1]])
    heros_used_percentage = "{0:.0f}".format(len(set(heros_played))/len(heros_all)*100) if heros_all else 0
    heros_all_count = len(heros_all)

    non_played_heros = [hero.name for hero in heros_all if hero not in heros_played]
    hero_games = {}
    hero_effectiveness = {}

    for game in games:
        if game.hero_1.name in hero_games:
            hero_games[game.hero_1.name]['games'] += 1
            if game.win:
                hero_games[game.hero_1.name]['games_won'] += 1
        else:
            hero_games[game.hero_1.name] = {'games': 1,
                                            'games_won': 0}
            if game.win:
                hero_games[game.hero_1.name]['games_won'] += 1

        if game.hero_2.name in hero_games:
            hero_games[game.hero_2.name]['games'] += 1
            if game.win:
                hero_games[game.hero_2.name]['games_won'] += 1
        else:
            hero_games[game.hero_2.name] = {'games': 1,
                                            'games_won': 0}
            if game.win:
                hero_games[game.hero_2.name]['games_won'] += 1

        if game.hero_3.name in hero_games:
            hero_games[game.hero_3.name]['games'] += 1
            if game.win:
                hero_games[game.hero_3.name]['games_won'] += 1
        else:
            hero_games[game.hero_3.name] = {'games': 1,
                                            'games_won': 0}
            if game.win:
                hero_games[game.hero_3.name]['games_won'] += 1

        if game.hero_4:
            if game.hero_4.name in hero_games:
                hero_games[game.hero_4.name]['games'] += 1
                if game.win:
                    hero_games[game.hero_4.name]['games_won'] += 1
            else:
                hero_games[game.hero_4.name] = {'games': 1,
                                                'games_won': 0}
                if game.win:
                    hero_games[game.hero_4.name]['games_won'] += 1

        if game.hero_5:
            if game.hero_5.name in hero_games:
                hero_games[game.hero_5.name]['games'] += 1
                if game.win:
                    hero_games[game.hero_5.name]['games_won'] += 1
            else:
                hero_games[game.hero_5.name] = {'games': 1,
                                                'games_won': 0}
                if game.win:
                    hero_games[game.hero_5.name]['games_won'] += 1

    for hero in hero_games:
        hero_effectiveness[hero] = hero_games[hero]['games_won'] / hero_games[hero]['games']

    max_effectiveness = max(hero_effectiveness.items(), key=operator.itemgetter(1))[1]

    best_heros = {}
    for hero in hero_effectiveness:
        if hero_effectiveness[hero] == max_effectiveness:
            best_heros[hero] = ["{0:.2f}".format(hero_effectiveness[hero]*100), hero_games[hero]['games_won'], hero_games[hero]['games']]

    masterminds_played = Counter([x.mastermind for x in games]).most_common(1)


    games_stats = {'games': len(games),
        'games_won': games_won,
        'percent_win': games_won_percentege,
        'solo_games': len(solo_games),
        'solo_games_percentege': solo_games_percentege,
        'solo_games_win': solo_games_win,
        'solo_games_win_percentage': "{0:.2f}".format(solo_games_win/len(solo_games)*100),
        'non_solo_games_win': non_solo_games_win,
        'non_solo_games_win_percentage': non_solo_games_win_percentage,
    }

    heros_stats = {
        'heros_used_count': len(set(heros_played)),
        'heros_all_count': heros_all_count,
        'heros_used_percentage': heros_used_percentage,
        'most_played_heros': most_played_heros,
        'most_played_heros_games_count': Counter(heros_played).most_common()[0][1],
        'non_played_heros': non_played_heros,
        'hero_eff': best_heros,
    }

    mastermind_stats = {
        'masterminds_played': masterminds_played,

    }

    return render(request, 'legendary/statistics.html', {'games': games_stats,
                                                         'heros_stats': heros_stats,
                                                         'mastermind_stats': mastermind_stats,
                                                         }
                  )
