class Menu:
    
    # MAIN_MENU_TEXT = """
    # Welcome to this program!

    # 1. Create a new object
    # 2. Print your object
    # 3. Delete your object"""


    # board = [[0 for y in range(4)] for x in range(10)]
    # print(board)
    row = 4
    column = 10

    def __init__(self):
        pass

    def print_seat(row, column):
        # b = [["[ ]" for y in range(row)] for x in range(column)]
        # print('\n'.join(map(str, b)))
        for y in range(10):
            print("\n")
            for x in range(4):
                print("[*]", end="")

    print_seat(2, 4)


        
    #print_seat()

    def main_menu_text(self):
        print("""
        Welcome to this program!

        1. Create a new object
        2. Print your object
        3. Delete your object
        
        """)