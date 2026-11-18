import os
from loading.loading_player import load_players
#This will be used also in the online mode
def load_teams(Player):
    #this is a dictionary that will keepthe name of the teams while loading
    load_team=[]
    with os.scandir("teams") as teams:
        for team in teams:
            if team.is_dir():
                load_team.append(team.name)
    return load_players(load_team,Player)