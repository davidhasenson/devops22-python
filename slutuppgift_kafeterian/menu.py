from dbmanager import *
from order import *
import os

class Menu:

    MAIN_MENU_TEXT = """
        Menu choices

        0. Quit
        1. Import a .csv file to beveragemenu
        2. Show beverage menu.
        3. Add order.
        4. Show orders
        5. Complete order
        6. random_beverage
        7. show_all_order
        8. show_completed_orders 
        9. delete_order
        10. order_served
        """
 
    def __init__(self):
        pass
 
    def user_input(self):
        try: # varför fungerar inte det?
            return int(input("Enter your choice [1-9]: "))
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
                Dbmanager().complete_order()
            elif choice == 6:
                Dbmanager().random_beverage()
            elif choice == 7:
                Dbmanager().show_all_orders()
            elif choice == 8:
                Dbmanager().show_completed_orders()
            elif choice == 9:
                Dbmanager().delete_order()
            elif choice == 10:
                Dbmanager().order_served()
            else:
                raise ValueError(f"Menu error. {choice} is not an option. ")
        except Exception as e:
            print(e)

    def menu_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_input()
            self.menu_choice(choice)
