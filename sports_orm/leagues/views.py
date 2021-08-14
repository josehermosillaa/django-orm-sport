from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		'consulta01': League.objects.filter(sport="Baseball"),
		'consulta02':League.objects.filter(name__contains="Women"),
		'consulta03':League.objects.filter(sport__contains="Hockey"),
		'consulta04':League.objects.exclude(sport="Football"),
		'consulta05':League.objects.filter(name__contains="Conference"),
		'consulta06':League.objects.filter(name__contains = "Atlantic"),
		'consulta07':Team.objects.filter(location__contains="Dallas"),
		'consulta08':Team.objects.filter(team_name__contains = "Raptors"),
		'consulta09':Team.objects.filter(location__contains="City"),
		'consulta10':Team.objects.filter(team_name__startswith="T"),
		'consulta11':Team.objects.order_by("location"),
		'consulta12':Team.objects.order_by("team_name").reverse(),
		'consulta13':Player.objects.filter(last_name__contains = "Cooper"),
		'consulta14':Player.objects.filter(first_name__contains = "Joshua"),
		'consulta15':Player.objects.filter(last_name__contains = "Cooper").exclude(first_name__contains="Joshua"),
		'consulta16':Player.objects.filter(Q(first_name__contains="Alexander")| Q(first_name__contains="Wyatt")),


	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")