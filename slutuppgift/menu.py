from main import *
#from loadstore import *
from dbhandler import *

class Menu:
    
    MAIN_MENU_TEXT = """
        Welcome to this program!

        0. quit
        1. Load a file to database
        2. Visa alla varor i sortimentet
        3. lägg till en vara i varukorgen
        4. ta bort en vara från varukorgen
        5. slutför beställning
        6. spara beställning 
        """

    def __init__(self):
        pass

    def __str__(self) -> str:
        print(f"-- menue string test --")

    def user_input(self):
        return int(input("Enter your choice [1-6]: "))

    def menu_choice(self, choice):
        if choice == 0:
            print("quitting program")
            self.running = False
        elif choice == 1:
            load_file_json()
        elif choice == 2:
            load_file_json_2()
        elif choice == 3:
            cur.execute(CREATE_TABLE_ITEMS)
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        else:
            print(f"{choice} is not an option")

    def menu_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_input()
            self.menu_choice(choice)


    def menu_test(self):
        print("menu test")
        

    




     