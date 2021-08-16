from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

from . import team_maker

def index(request):
	lvl2tarea14all = Team.objects.annotate(Count('all_players'))
	print(lvl2tarea14all[0].all_players)
	final = {}
	for team in lvl2tarea14all:
		if team.all_players__count > 11:
			final[team.team_name] = team.all_players__count
			print(team.team_name, " ", team.all_players__count)
		#print(team.team_name, " ",team.all_players__count + team.curr_players__count)
		#print(team.team_name, " ", team.all_players__count)
	print(final)

	dconsulta15 = Player.objects.annotate(Count('all_teams'))
	print(dconsulta15)
	dconsulta15ordered = dconsulta15.order_by('-all_teams__count')
	print(dconsulta15ordered)

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
		'2consulta01':Team.objects.filter(league=League.objects.get(name="Atlantic Soccer Conference")),
		'2consulta02':Player.objects.filter(curr_team=Team.objects.get(location = "Boston", team_name = "Penguins")),
		'2consulta03':Player.objects.filter(curr_team__in=Team.objects.filter(league__in=(League.objects.filter(name="International Collegiate Baseball Conference")))),
		'2consulta04':Player.objects.filter(curr_team__in=Team.objects.filter(league__in=(League.objects.filter(name="American Conference of Amateur Football")))),
		'2consulta05':Player.objects.filter(all_teams__in=Team.objects.filter(league__in=(League.objects.filter(sport='Soccer')))),
		'2consulta06':Team.objects.filter(curr_players__in=Player.objects.filter(first_name="Sophia")),
		'2consulta07':League.objects.filter(teams__in = Team.objects.filter(curr_players__in=Player.objects.filter(first_name="Sophia"))),
		'2consulta08':Player.objects.filter(last_name="Flores", curr_team__in=Team.objects.exclude(location="Washington", team_name="Roughriders")),
		'2consulta09':Team.objects.filter(all_players =Player.objects.get(first_name="Samuel", last_name="Evans")),
		'2consulta10':Team.objects.get(location="Manitoba").all_players.all(),
		'2consulta11':list(set(Team.objects.get(location="Wichita", team_name="Vikings").all_players.all())-set(Team.objects.get(location="Wichita", team_name="Vikings").curr_players.all())),
		'2consulta12':Player.objects.get(first_name="Jacob", last_name="Gray").all_teams.all().exclude(location="Oregon", team_name="Colts"),
		'2consulta13': Player.objects.filter(all_teams__in =Team.objects.filter(league__in=(League.objects.filter(name="Atlantic Federation of Amateur Baseball Players")))).filter(first_name="Joshua"),
		'2consulta14':final,
		'2consulta15':dconsulta15ordered


	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")