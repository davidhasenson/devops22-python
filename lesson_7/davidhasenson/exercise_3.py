# Create a function that returns a integer
from timeit import repeat


def return_int():
    return 1
print(return_int())

# Create a function that returns a tuple with (x, y) value
def my_tuple(x,y):
    return x, y
print(my_tuple("hello", "world"))

# Create a function that returns a boolean value
def my_boolean():
    return True
print(my_boolean())

# Create a function that returns a float
def my_float():
    return 1.0
print(my_float())

# Create a function that has firstname and lastname as parameters and returns fullname.
def fullname(firstname, lastname):
    return firstname + " " + lastname
print(fullname("Homer", "simpsons"))

# Create a function that calculates the area of a rectangle and returns the result
def rectangle_area_calculation(width, length):
    return width * length
print(rectangle_area_calculation(2,4))

# Create a function that expects a list as argument, the list should contain integers and the function should return the sum of all elements in the list.
list_1 = [1,2,3,4]
def sum_int_list(my_list=[]):
    return sum(my_list)
print(sum_int_list(list_1))

# Create a function that repeats a word multiple time, word and repeat is used as parameters. If the word is hello and repeat is 3, it will print hello three times.
def repeat_word(word, repeat):
    return word * int(repeat)
print(repeat_word("Hello world ", 3))

    
