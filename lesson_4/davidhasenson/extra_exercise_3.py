# Skriv ett program som låter användaren gissa vilket tal du tänker på tills användaren gissar rätt.
# Talet har du hårdkodat in i programmet och gissningen från användaren hämtas in via
# input gång på gång tills dess att gissning == input.
"""
number = int(input("Enter an integer: "))
if number != 42:
    print("Congratulations, you're correct! ")
elif number < 42:
    print("Wrong, it's higher. ")
elif number > 42:
    print("Wrong, it's lower. ")
else:
    print("Error")
"""

number = 0
while number != 42:
    number = int(input("Enter an integer: "))
    if number < 42:
        print("Wrong, it's higher. ")
    if number > 42:
        print("Wrong, it's lower. ")
else:
    print("Congratulations, you're correct! ")
