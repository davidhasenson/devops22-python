# Du har följande lista på frukter:
# fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
# Skriv ett program som frågar användaren efter hur många platser för frukt hen har i sin
# korg, och sedan fyller du denna korg (en lista) med frukter genom att loopa igenom
# frukt-listan tills dess att korg-listan är full.
# Output-exempel:
# My_basket = ['apple', 'orange', 'pear', 'banana', 'grapes', 'apple','orange', 'pear']

fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
my_basket = []
y = 0

nr_fruits = int(input("Hur många platser har du för frukt i din korg? "))
for x in range(nr_fruits):
    # print(x)

    my_basket.append(fruits[y])
    y += 1
    if y == 5:
        y =0 

print(f"My_basket = {my_basket}")
