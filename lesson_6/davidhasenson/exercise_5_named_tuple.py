from collections import namedtuple


my_Coordinates = namedtuple("Coordinates", ["x","y"])
c = my_Coordinates(x=5, y=3)

board = [["-"]*10 for i in range(10)]

board[c.x][c.y] = "*"

for row in board:
    print(row)

board[1][2] = "*"
board[4][6] = "*"

#print(board)

# Calculate the Euclidean distance (hypotenuse) 
