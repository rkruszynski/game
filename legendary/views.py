from django.shortcuts import render, get_object_or_404

from .models import Hero, Team, Mastermind, Scheme, Game
from django.http import Http404, HttpResponseRedirect
from .forms import HeroForm, TeamForm, MastermindForm, SchemeForm, GameForm
from django.contrib import messages
from django.db.models import Q
from collections import Counter


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
                                                          'stats': stats})


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
        schemes = Scheme.objects.order_by('name')
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
