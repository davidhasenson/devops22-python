# Exercise 4 Sum
# Write a program that fulfills the specification:

# Ask the user for a start and stop integer
#start_int, stop_int = int(input("write a start integer and a stop integer: "))
start_int = int(input("Enter a start integer: "))
stop_int = int(input("Enter a stpo integer: "))

# Print every integer between start and stop. i.e. start = 1, stop = 5 would print:
number = start_int
while number < stop_int:
    print(number)
    number +=1

# eller så här
for x in range(start_int, stop_int):
    print(x)

# Print the sum of all integers i.e
number = start_int
sum = 0
while number < stop_int:
    sum = sum + number
    number +=1
print(f"Sum: {sum}")