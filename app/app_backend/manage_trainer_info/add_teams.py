from APPLICACION_DE_BALONCESTO__GODOT_DE_BALONCESTO_.py import trainer_info
import os
def add_teams_locally(team_name):
    trainer_info.trainer_teams[team_name]={}
    team_path=os.path.join("teams",team_name)
    os.makedirs(team_path)