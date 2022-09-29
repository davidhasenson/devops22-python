from main import *
#from loadstore import *
#from dbhandler import *

class Menu:
    
    MAIN_MENU_TEXT = """
        Welcome to this program!

        0. quit
        1. Load a file to database (import_csv_file())
        2. Visa alla varor i sortimentet
        3. lägg till vara till sortimentet
        4. lägg till en vara i varukorgen
        5. ta bort en vara från varukorgen
        6. slutför beställning
        7. spara beställning 
        """

    def __init__(self):
        pass

    def __str__(self) -> str:
        pass

    def user_input(self):
        return int(input("Enter your choice [1-6]: "))

    def menu_choice(self, choice):
        if choice == 0:
            print("quitting program")
            self.running = False
        elif choice == 1:
            import_csv_file()
        elif choice == 2:
            get_all_items()
        elif choice == 3:
            add_item()
        elif choice == 4:
            add_to_cart()
        elif choice == 5:
            delete_from_cart()
        elif choice == 6:
            close_cart()
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
        

    




     