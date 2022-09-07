# Write a program that handles salary negotiations. The user is the employee and the boss is your program.
salary = 30000
percent = 0

# The boss tells the user it's current salary and currency
print("Your current salary is %d \N{euro sign}"%salary)
# The employee ask for more money with an input. I.e 2000 more
rise = 2000 #int(input("How much more do you want? "))
# The boss calculates the percentage salary increase and respond with a emoji. And always respond NO to the initial proposal.
percent = rise/(salary/100) 
print(f"\N{money-mouth face} NO")
# The employee ask again for another amount i.e 1800
rise = 1800 #int(input("How much more do you want?"))
