# Exercise 5 Until stop
# Write a program that fulfills the specification:

# Create a while loop that runs forever
while 0 < 1:

# In each iteration, input a text
    word = input("Write something: ")

# In each iteration, print a text "Enter stop to quit: "
    print("Enter stop to quit. ")

# If the text equals stop, break the while loop
    if word == "stop":
        break

# If the text don't equals stop, print the text and the length of the text
    else:
        print(f"{word} {len(word)}")