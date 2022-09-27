class Person:

    def __init__(self, firstname, birthdate):
        self.firstname = firstname
        self.birthdate = birthdate

    def __str__(self):
            return f"{self.firstname} {self.birthdate}"

    def hello(self):
        print ("hello") 