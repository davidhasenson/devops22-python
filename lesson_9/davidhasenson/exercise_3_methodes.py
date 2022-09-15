class MyClass:

    def _init_(self, my_arg):
        self.my_arg = my_arg

    def my_method(self):
        return self.my_arg * 2

class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side **2 
        return float(area)

    def circumference(self):
        circumference = self.side * 4
        return float(circumference)

if __name__ =="__main__":

    square_1 = Square(2)
    print(square_1.area())
    print(square_1.circumference())

    square_2 = Square(3.5)
    print(square_2.area())
    print(square_2.circumference())