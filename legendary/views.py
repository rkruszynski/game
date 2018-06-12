from django.shortcuts import render, get_object_or_404

from .models import Hero, Team, Mastermind, Scheme
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .forms import HeroForm, TeamForm, MastermindForm, SchemeForm
from django.contrib import messages



# Create your views here.


def index(request):
    heros = Hero.objects.order_by('name')
    template = loader.get_template('legendary/index.html')
    context = {
        'heros': heros
    }
    return HttpResponse(template.render(context, request))


def hero_detail(request, hero_id):
    try:
        hero = Hero.objects.get(pk=hero_id)
    except Hero.DoesNotExist:
        raise Http404("Hero does not exist!")
    return render(request, 'legendary/hero_detail.html', {'hero': hero})


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
    teams = Team.objects.order_by('name')
    return render(request, 'legendary/teams.html', {'teams': teams})


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
