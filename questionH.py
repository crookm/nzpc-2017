'''
League Football. Ew.
Author: Gina
'''

##class Team:
##    def __init__(self, team):
##        self.name = team[0]
##        self.games_played = int(team[1])
##        self.wins = int(team[2])
##        self.draws= int(team[3])
##        self.losses= int(team[4])
##        self.goals_for= int(team[5])
##        self.goals_against= int(team[6])
##        self.points =int(team[7])
##
##    def __repr__(self):
##        return "Team", self.name, ": games, wins, draws, losses, goalsfor, goalsa, point"
##
##    def __str__(self):
##        return "This is a string object"

   
def input_teams():

    num_teams = int(input())
    teams_list =[]
    for i in range(num_teams):
        name = input()
        score = input()
        team = name+" "+score
        team = team.split()
        for i in range(1,8):
            team[i] = int(team[i])    
            
        teams_list.append(team)
    
    return teams_list


def make_changes(teams_dict):
    num_changes = int(input())
    for i in range(num_changes//2):
        hometeam = input()
        hometeam_score = int(input())
        awayteam = input()
        awayteam_score = int(input())
        

        

    
    
    
def main():
    teams_list = input_teams()
    print(teams_list)
    #make into dictionary
    teams_dict = {}
    for i in teams_list:
        teams_dict[i[0]] = i
    
    print(teams_dict)   
        
    make_changes(teams_dict)
    teams_list.sort(key = lambda x : x[-1])
    
    
    


main()

        
