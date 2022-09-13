# Create a function that prints 1 to 10 by default, i.e start=1 stop=11 and uses a range in the function block.
def print_numbers(start=1, stop=11):
    for i in range(start, stop):
        print(i)
print_numbers()        


# Create a function that by default prints a string, if reverse=True is used as argument the string is printed in reverse.
def srting_reverse(word, reverse=False):
    if reverse:
        print("".join(list(reversed(word))))
    else:
        print(word)
srting_reverse("hello", True)
srting_reverse("hello", False)
