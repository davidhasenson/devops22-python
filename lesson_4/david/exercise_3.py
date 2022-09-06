# Exercise 3 Repeat word
# Write a program that fulfills the specification:"

# Ask the user for a word
word = input("write a word: ")

# Print the word x times, where x = len(word). i.e if the word is hello the program writes:
# hello
# hello
# hello
# hello
# hello

x = len(word)
for x in range (x):
    print(word)