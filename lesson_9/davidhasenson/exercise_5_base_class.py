import random 

class Person:

    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

class player(Person):

    def __init__ (self, name, year_of_birth, speed, agility, strenght):
        super().__init__(name, year_of_birth)
        self.speed = speed
        self.agility = agility
        self.strenght = strenght

class Coach(Person):

    def __init__(self, name, year_of_birth, voice_level):
        super().__init__(name, year_of_birth)
        self.voice_level = voice_level 

class Team:

    def __init__(self, players, coach):
        self.players = players
        self.coach = coach

    def summerize_team(self):
        team = " My team "
        team += f"Coach {self.coach}\n"
        team += "Players \n"
        team += "\n".join(map(str, self.players))
        return team

def random_level():
    return random.randint(1, 10)

def main():
    coach = Coach("Max", 1999, 7)
    
    players = []
    for name in ["lisa", "eva", "petra", "linda", "amanda", "jonna", "malin", "fredrika", "frida", "jenny"]:
        year_of_birth = 1949
        players.append(player(name, year_of_birth, random_level() ,random_level() , random_level() ))

    team = Team(players, coach)
    print(team.summerize_team())

if __name__=="__main__":
    main()