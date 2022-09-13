# Create a function with name do_nothing
# The function should have a pass
# Call the function from your code
def do_nothing():
    pass

print(do_nothing)

# Functions getting started:
# Create a function that prints hello world

def hello():
    print("hello world")

hello()
# Create a function that prints the result from 1 == 1.0
def one_one_dot():
    print(1 == 1.0)

one_one_dot()
# Create a function that prints the alphabet in reverse order
import string
def alphabet_reverse():
    print(string.ascii_lowercase[::-1])
alphabet_reverse()

# Functions with arguments
# Create a function that prints hello name with name as a parameter
def hello_name(name, greeting="hello"):
    print(f"{greeting} {name}")
hello_name("max")

# Create a function that prints a string in capital letters, with word as a parameter
def capiytal_string(word):
    print(f"{word.capitalize()} ")
capiytal_string("hej")

# Create a function that prints numbers between 1 and stop, where stop is a parameter
def print_numbers(stop, start=1):
    for i in range(start, stop):
        print(i)
print_numbers(10)