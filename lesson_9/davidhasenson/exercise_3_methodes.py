class MyClass:

    def _init_(self, my_arg):
        self.my_arg = my_arg

    def my_method(self):
        return self.my_arg * 2

class Square:

    def __init__(self, side):
        self.side = side

    def area(side):
        area = side **2 
        return float(area)

    def circumference(side):
        circumference = side * 4
        return float(circumference)

if __name__ =="__main__":
    # my_oject = MyClass("args")
    # print(my_class.my_method())

    # my_another_object = My_Class("args")
    # print(my_another_object.my_method())

    my_test = Square(2)
    #print(my_test.area())
    print(my_test.circumference())