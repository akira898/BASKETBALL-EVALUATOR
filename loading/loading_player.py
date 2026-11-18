import os
def load_players(teams,Player):
    loading_dict={}
    for i in teams:
        team_loading=i
        loading_dict[team_loading]={}
        search_path=os.path.join("teams",i)
        for z in os.listdir(search_path):
            #z is the name of the player
            #player_info will have everything about the player that the program is currently loading
            player_info=Player(z,"","0")
            loading_dict[team_loading][player_info.player_name]={}
            player_path=os.path.join("teams",i,z)
            with open(player_path,"r")as inf:
                info=inf.read().split()
                player_info.player_image=info[0]
                player_info.player_high=float(info[1])
                loading_dict[team_loading][z]["image"]=player_info.player_image
                loading_dict[team_loading][z]["heith"]=player_info.player_high
    return loading_dict