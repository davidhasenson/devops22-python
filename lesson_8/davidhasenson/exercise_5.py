my_numbers = list(range(1, 11))
my_lamda = lambda x: x + 1
add_one = list(map(my_lamda, my_numbers))

print(add_one[1:])