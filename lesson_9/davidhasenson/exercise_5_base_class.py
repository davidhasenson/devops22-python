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
        self.player = players
        self.coach = coach

def main():
    team_coach = Coach("Max", 1999, 7)

    team_players = []
    for name in ["lisa", "eva", "petra", "linda", "amanda", "jonna", "malin", "fredrika", "frida", "jenny"]:
    

if __name__=="--main_":
    main()