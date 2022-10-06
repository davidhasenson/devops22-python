from dbmanager import *
from order import *
import os

class Menu:

    MAIN_MENU_TEXT = """
        Menu choices

        0.  Quit
        1.  Import a .csv file to beveragemenu.
        2.  Add item to menu. 
        3.  Show beverage menu.
        4.  Delete item from menu.
        5.  Add order.
        6.  Order random beverage.
        7.  Mark order as received.
        8.  Mark order as finished.
        9.  Mark order as served.
        10. Show all orders.
        11. Show received orders.
        12. Show finished orders.
        13. Show served orders.
        14. Delete order.        
        """
 
    def __init__(self):
        pass
 
    def user_input(self):
        try: 
            return int(input("Enter your choice [1-14]: "))
        except ValueError as v:
            print(v)
            print("You must enter an integer. ")

    def menu_choice(self, choice):
        try:
            if choice == 0:
                print("quitting program")
                self.running = False
            elif choice == 1:
                Dbmanager().import_csv_file_to_db()
            elif choice == 2:
                Dbmanager().add_menu_item()
            elif choice == 3:
                Dbmanager().view_menu()
            elif choice == 4:
                Dbmanager().delete_menu_item()
            elif choice == 5:
                Dbmanager().add_order()
            elif choice == 6:
                Dbmanager().random_beverage()
            elif choice == 7:
                Dbmanager().order_received()
            elif choice == 8:
                Dbmanager().order_finished()
            elif choice == 9:
                Dbmanager().order_served()
            elif choice == 10:
                Dbmanager().show_all_orders()
            elif choice == 11:
                Dbmanager().show_received_orders()
            elif choice == 12:
                Dbmanager().show_finished_orders()
            elif choice == 13:
                Dbmanager().show_served_orders()
            elif choice == 14:
                Dbmanager().delete_order()
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
