from math import sqrt
from collections import namedtuple

my_Coordinates = namedtuple("Coordinates", ["x","y"])

point_1 = my_Coordinates(x=2, y=3)
point_2 = my_Coordinates(x=5, y=7)

board = [["-"]*10 for i in range(10)]

board[point_1.x][point_1.y] = "*"
board[point_2.x][point_2.y] = "*"

for row in board:
    print(row)

# Calculate the Euclidean distance (hypotenuse) d = √[ (x2 – x1)2 + (y2 – y1)2]
calculate_distance = sqrt(((point_2.x - point_1.x)**2) + ((point_2.y - point_1.y)**2))
print(calculate_distance)
