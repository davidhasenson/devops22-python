from person import *
from menu import *

def main():
    person = Person("john", 1854)
    print(person)
    person.hello()
    menu = Menu()
    menu.main_menu_text()
    menu.print_seat(4, 10)


if __name__ == "__main__":
    main()

