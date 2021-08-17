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
		'l2consulta01':Team.objects.filter(league__name="Atlantic Soccer Conference"),
		# 'l2consulta02':Player.objects.filter(curr_team=Team.objects.get(location = "Boston", team_name = "Penguins")),
		'l2consulta02':Player.objects.filter(curr_team__team_name="Penguins", curr_team__location="Boston"),
		# 'l2consulta03':Player.objects.filter(curr_team__in=Team.objects.filter(league__in=(League.objects.filter(name="International Collegiate Baseball Conference")))),
		'l2consulta03':Player.objects.filter(curr_team__league__name = "International Collegiate Baseball Conference"),
		# 'l2consulta04':Player.objects.filter(curr_team__in=Team.objects.filter(league__in=(League.objects.filter(name="American Conference of Amateur Football")))),
		'l2consulta04':Player.objects.filter(curr_team__league__name = "American Conference of Amateur Football").filter(last_name = "Lopez"),
		# 'l2consulta05':Player.objects.filter(all_teams__in=Team.objects.filter(league__in=(League.objects.filter(sport='Soccer')))),
		'l2consulta05':Player.objects.filter(curr_team__league__sport="Football"),
		# 'l2consulta06':Team.objects.filter(curr_players__in=Player.objects.filter(first_name="Sophia")),
		'l2consulta06':Team.objects.filter(curr_players__first_name="Sophia"),
		# 'l2consulta07':League.objects.filter(teams__in = Team.objects.filter(curr_players__in=Player.objects.filter(first_name="Sophia"))),
		'l2consulta07':League.objects.filter(teams__curr_players__first_name="Sophia"),
		# 'l2consulta08':Player.objects.filter(last_name="Flores", curr_team__in=Team.objects.exclude(location="Washington", team_name="Roughriders")),
		'l2consulta08':Player.objects.exclude(curr_team__team_name="Roughriders", curr_team__location="Washington").filter(last_name="Flores"),
		# 'l2consulta09':Team.objects.filter(all_players =Player.objects.get(first_name="Samuel", last_name="Evans")),
		'l2consulta09': Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans") ,
		# 'l2consulta10':Team.objects.get(location="Manitoba").all_players.all(),
		'l2consulta10': Player.objects.filter(all_teams__team_name="Tiger-Cats", all_teams__location="Manitoba"),
		# 'l2consulta11':list(set(Team.objects.get(location="Wichita", team_name="Vikings").all_players.all())-set(Team.objects.get(location="Wichita", team_name="Vikings").curr_players.all())),
		'l2consulta11': Player.objects.filter(all_teams__team_name="Vikings").exclude(curr_team__team_name="Vikings").filter(all_teams__location="Wichita").exclude(curr_team__location="Wichita"),
		# 'l2consulta12':Player.objects.get(first_name="Jacob", last_name="Gray").all_teams.all().exclude(location="Oregon", team_name="Colts"),
		'l2consulta12': Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(curr_players__first_name="Jacob", curr_players__last_name="Gray"),
		# 'l2consulta13': Player.objects.filter(all_teams__in =Team.objects.filter(league__in=(League.objects.filter(name="Atlantic Federation of Amateur Baseball Players")))).filter(first_name="Joshua"),
		'l2consulta13': Player.objects.filter(first_name = "Joshua",all_teams__league__name="Atlantic Federation of Amateur Baseball Players"),
		'l2consulta14':Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12),
		'l2consulta15': Player.objects.all().annotate(num_teams=Count('all_teams')).order_by('num_teams'),


	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")