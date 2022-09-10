# Write a program that handles salary negotiations. The user is the employee and the boss is your program.
salary = 30000
rise = 0

# The boss tells the user it's current salary and currency
print("Your current salary is %d \N{euro sign}"%salary)

# The employee ask for more money with an input. I.e 2000 more
rise = 2000 #int(input("How much more do you want? "))

# The boss calculates the percentage salary increase and respond with a emoji. And always respond NO to the initial proposal.
requested_salery = salary + rise
percentage_salery_increase = ((requested_salery * 100) / salary) - 100
print(f"\N{money-mouth face} NO, percentage salary increase is {percentage_salery_increase} ")

# The employee ask again for another amount i.e 1800
i = 0
number_of_iterations = 0
while i == 0:
    rise = input("How much more do you want? (Write stop to quit.) ")
    requested_salery = salary + int(rise)
    percentage_salery_increase = ((requested_salery * 100) / salary) - 100

    if rise == "stop":
        break
    elif percentage_salery_increase > 2:
        print(f"{percentage_salery_increase} % NO, too much. try again.")
    else:
        print(f"{percentage_salery_increase} % Yes, you win. ")
        break
    number_of_iterations += 1
    if number_of_iterations == 5: 
        print("Too many tries, no deal.")
        break