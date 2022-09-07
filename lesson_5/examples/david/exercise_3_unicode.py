# How to write a euro sign can be found at [Currency Symbols](https://www.unicode.org/charts/PDF/U20A0.pdf). 
# How to write emoji can be found at [emoji](https://unicode.org/emoji/charts/full-emoji-list.html), 
# you can also check the formal charts for [symbols](https://www.unicode.org/charts/#symbols) 
# you use either name or code: \N{money-mouth face}, or code \U0001F911

# Write a program that fulfills the specification
# Let the user input a price, i.e Your new car cost: 1000000
price = int(input("Your new car cost: "))
# Add a currency symbol (not dollar) to the input string. ie. Your new car cost [$]
cost = str(price) + " \u20AC" + "\N{euro sign}"
print(cost)
# Depending on the price, respond with a matching emoji (you decide which ones) 
# i.e if cost below 50000 use one emoji, if is above another one
if price > 50000:
    print("\U0001F631 \N{face screaming in fear}")
else:
    print("\U0001F60E \N{smiling face with sunglasses}")