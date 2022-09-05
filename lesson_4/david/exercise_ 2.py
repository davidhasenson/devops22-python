# Write a program that fulfills the specification:

# Ask the user for a name
new_name = max #input("Write your name: ").lower

# Create a tuple with at least five names
name_tuple = ("max", "john", "oliver", "will", "adam" )
print(name_tuple)

# If the user input is in the tuple, print the text "Welcome {name} your are on the list".
if new_name in name_tuple:
    print("Welcome {new_name} your are on the list")

# If the user input is not in the tuple, print "Sorry, you are not on the list".
else:
    print("Sorry, you are not on the list")