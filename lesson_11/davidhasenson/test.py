
# with open("lesson_11/davidhasenson/person.csv", "r") as file:
#     nr_records = 0
#     for row in file:
#         cur.execute("INSERT INTO persons VALUES (?,?,?,?,?)", row.split(","))
#         conn.commit()
#         nr_records += 1
# conn.close()
# print("\n {} records transferred ".format(nr_records))


class Menu:

    MAIN_MENU_TEXT = """
    Welcome to this program!

    1. Create a new object
    2. Print your object
    3. Delete your object
    
    type q or Q to delete
    """

    def user_choice(self):
        return input("Enter your choice 1-3 or q: ")

    def wait_for_user(self):
        if self.running:
            input("Please press any key to continues.")

    def menu_commands(self, choice):
        if choice == 'q' or choice == 'Q':
            self.running = False
        elif choice == "1":
            print("hello")
        elif choice == "2":
            print("world")
        elif choice == "3":
            print("hello world")

    def start_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_choice()
            self.menu_commands(choice)
            self.wait_for_user()

Menu().start_loop()