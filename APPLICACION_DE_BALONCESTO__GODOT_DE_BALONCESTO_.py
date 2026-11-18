from loading.loading_teams import load_teams
class Player:
    def __init__(self,player_name,player_image,player_high):
        self.player_name=player_name
        self.player_image=player_image
        self.player_high=player_high


class Trainer:
    def __init__(self,trainer_username,trainer_teams):
        self.trainer_user=trainer_username
        self.trainer_teams=trainer_teams
    def add_team(self,trainer_teams):
        self.trainer_teams[input()]=""
trainer_info=Trainer("",load_teams(Player))                                         
print(trainer_info.trainer_teams,trainer_info.trainer_user)
