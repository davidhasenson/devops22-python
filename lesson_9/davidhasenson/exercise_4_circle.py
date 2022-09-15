from math import pi

class Circle:
    
    def __init__(self, diagonal):
        self.diagonal = diagonal
        self.area = self.calc_area()
        self.circumference = self.calc_circumference()
        self.color = "grey"

    def calc_area(self):
        return pi * (self.diagonal / 2) **2
    
    def calc_circumference(self):
        return pi * self.diagonal

    def set_color(self, color):
        self.color = color

def main():
    my_circle = Circle(2)
    print(my_circle.area)
    print(my_circle.circumference)
    print(my_circle.color)
    my_circle.set_color("red")
    print(my_circle.color)


if __name__ =="__main__":
    main()

    