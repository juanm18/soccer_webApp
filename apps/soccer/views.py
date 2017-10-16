from django.shortcuts import render
from datetime import datetime
import httplib
import requests
import json


# Create your views here.
def index(request):
    connection = httplib.HTTPSConnection('api.football-data.org')
    headers = {
        'X-Auth-Token': 'b9b821adb4414d58b06b8a48b0de1dc2',
        'X-Response-Control': 'minified'
        }
    connection.request('GET', '/v1/competitions', None, headers )
    response = connection.getresponse()
    # print response.status, response.reason
    data = response.read().decode('utf-8')
    all_leagues = json.loads(data)
    return render(request,"index.html",{'all_leagues':all_leagues})

def leagues(request,id):
    # League Table data
    conn = httplib.HTTPSConnection('api.football-data.org')
    headers = {
        'X-Auth-Token': 'b9b821adb4414d58b06b8a48b0de1dc2',
        'X-Response-Control': 'minified'
        }
    conn.request('GET', '/v1/competitions/'+id+'/leagueTable', None, headers )
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    my_league_table = json.loads(data)
    # print my_league_table

    #League Data
    connection = httplib.HTTPSConnection('api.football-data.org')
    headers = {
        'X-Auth-Token': 'b9b821adb4414d58b06b8a48b0de1dc2',
        'X-Response-Control': 'minified'
        }
    connection.request('GET', '/v1/competitions/'+id, None, headers )
    response = connection.getresponse()
    data = response.read().decode('utf-8')
    my_league = json.loads(data)


    connection = httplib.HTTPSConnection('api.football-data.org')
    headers = {
    'X-Auth-Token': 'b9b821adb4414d58b06b8a48b0de1dc2',
    'X-Response-Control': 'minified'
    }
    connection.request('GET', '/v1/competitions/'+id+'/fixtures', None, headers )
    response = connection.getresponse()
    data = response.read().decode('utf-8')
    league_fixtures = json.loads(data)
    # print league_fixtures
    # print league_fixtures

    current_match_day_dict={}
    current_match_day_fixture = []
    for match in league_fixtures:
        var = league_fixtures[match]
    for i in var:
        if i['matchday'] == my_league['currentMatchday']:
            date = i['date'].replace('Z','')
            date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
            date = date.strftime("%Y-%m-%d %I:%M:%S")
            home = i['homeTeamName']
            away = i['awayTeamName']

            current_match_day_dict = {
            'homeTeam': home,
            'awayTeam': away,
            'gameDate': date,
            }

            current_match_day_fixture.append(current_match_day_dict)

    print current_match_day_fixture
    #All Teams Data
    connect = httplib.HTTPSConnection('api.football-data.org')
    headers = {
        'X-Auth-Token': 'b9b821adb4414d58b06b8a48b0de1dc2',
        'X-Response-Control': 'minified'
        }
    connect.request('GET', '/v1/competitions/'+id+'/teams', None, headers )
    response = connect.getresponse()
    data = response.read().decode('utf-8')
    all_teams = json.loads(data)

    return render(request,'league.html',{'current_match_day_fixture':current_match_day_fixture, 'all_teams':all_teams,'league_fixtures':league_fixtures, 'my_league':my_league, 'my_league_table':my_league_table})



def teams(request,id):
        connection = httplib.HTTPSConnection('api.football-data.org')
        headers = {
            'X-Auth-Token': 'b9b821adb4414d58b06b8a48b0de1dc2',
            'X-Response-Control': 'minified'
            }
        connection.request('GET', '/v1/teams/'+id, None, headers )
        response = connection.getresponse()
        data = response.read().decode('utf-8')
        my_team = json.loads(data)
        print my_team

        connection = httplib.HTTPSConnection('api.football-data.org')
        headers = {
            'X-Auth-Token': 'b9b821adb4414d58b06b8a48b0de1dc2',
            'X-Response-Control': 'minified'
            }
        connection.request('GET', '/v1/teams/'+id+'/fixtures', None, headers )
        response = connection.getresponse()
        data = response.read().decode('utf-8')
        my_team_fixtures = json.loads(data)

        connection = httplib.HTTPSConnection('api.football-data.org')
        headers = {
            'X-Auth-Token': 'b9b821adb4414d58b06b8a48b0de1dc2',
            'X-Response-Control': 'minified'
            }
        connection.request('GET', '/v1/teams/'+id+'/players', None, headers )
        response = connection.getresponse()
        data = response.read().decode('utf-8')
        my_team_players = json.loads(data)

        return render(request,'teams.html',{'my_team':my_team, 'my_team_fixtures':my_team_fixtures, 'my_team_players':my_team_players})


def champions(request,id):
    conn = httplib.HTTPSConnection('api.football-data.org')
    headers = {
        'X-Auth-Token': 'b9b821adb4414d58b06b8a48b0de1dc2',
        'X-Response-Control': 'minified'
        }
    conn.request('GET', '/v1/competitions/'+id, None, headers )
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    my_league = json.loads(data)
    conn = httplib.HTTPSConnection('api.football-data.org')
    headers = {
    'X-Auth-Token': 'b9b821adb4414d58b06b8a48b0de1dc2',
    'X-Response-Control': 'minified'
    }
    conn.request('GET', '/v1/competitions/'+id+'/teams', None, headers )
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    my_league_teams = json.loads(data)

    conn = httplib.HTTPSConnection('api.football-data.org')
    headers = {
        'X-Auth-Token': 'b9b821adb4414d58b06b8a48b0de1dc2',
        'X-Response-Control': 'minified'
        }
    conn.request('GET', '/v1/competitions/'+id+'/leagueTable', None, headers )
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    my_league_table = json.loads(data)
    print my_league_table

    conn = httplib.HTTPSConnection('api.football-data.org')
    headers = {
        'X-Auth-Token': 'b9b821adb4414d58b06b8a48b0de1dc2',
        'X-Response-Control': 'minified'
        }
    conn.request('GET', '/v1/competitions/'+id+'/fixtures', None, headers )
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    my_league_fixtures = json.loads(data)

    return render(request,'champions.html',{'my_league':my_league, 'my_league_teams':my_league_teams, 'my_league_table':my_league_table, 'my_league_fixtures':my_league_fixtures})
