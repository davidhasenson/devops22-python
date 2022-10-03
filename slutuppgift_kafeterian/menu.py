from dbmanager import *
import os

class Menu:

    MAIN_MENU_TEXT = """
        Welcome to this program!

        0. quit
        1. Load a file to database (import_csv_file())
        2. Visa meny.
        3. add_order
        4. show_orders
        5. ta bort en vara från varukorgen
        6. slutför beställning
        7. Dbmanager().delete_db() 
        """
 
    def __init__(self):
        pass
 
    def user_input(self):
        try: # varför fungerar inte det?
            return int(input("Enter your choice [1-6]: "))
        except ValueError as v:
            print(v)
            print("du måste ange en integer. ")

    def menu_choice(self, choice):
        try:
            if choice == 0:
                print("quitting program")
                self.running = False
            elif choice == 1:
                Dbmanager().import_csv_file_to_db()
            elif choice == 2:
                Dbmanager().view_menu()
            elif choice == 3:
                Dbmanager().add_order()
            elif choice == 4:
                Dbmanager().show_orders()
            elif choice == 5:
                pass
            elif choice == 6:
                pass
            elif choice == 7:
                pass
            else:
                raise ValueError("efe")
        except Exception as e:
            print(e)
            print(f"menu error. {choice} is not an option")


    def menu_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_input()
            self.menu_choice(choice)
