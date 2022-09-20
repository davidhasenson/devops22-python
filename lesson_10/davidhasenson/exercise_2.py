


class Animal:
    
    def __init__(self) -> None:
        pass

    def animal_type(self, type):
        self.type = type

    def print_animal(self):
        print(self.type)

class Menu:

    main_menu_text = """
'-------------------------'
'------- Main Menu -------'
'-------------------------'

1: 'Create object',
2: 'Print object',
3: 'Delete object'
"""
    def __init__(self):
        self.run = False
        self.main_nemu_commands = {1: self.cmd_create_object, 
                                    2: self.cmd_print_object, 
                                    3: self.cmd_delete_object} 

    def cmd_create_object (self, type):
        self.my_object = Animal(type)


    def cmd_print_object(self):
        print(self.print_animal)

    def cmd_delete_object(self):
        del(self.my_object)

    def user_input(self):
        return int(input("Enter your choice [1-3]: "))

    def menu_loop(self):
        self.run = True
        while self.run:
            print(Menu.main_menu_text)
            chois = self.user_input()
            self.execute_command(self.main_nemu_commands, chois)


if __name__ == "__main__":
    Menu().menu_loop()