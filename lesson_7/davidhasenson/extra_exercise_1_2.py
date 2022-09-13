# Skapa ett program utan funktioner som tar ett heltal som input och sedan skriver ut följande:
# Om talet är större än 5: En sträng bestående av talet som är lika lång som talet. Ex:
# Ange ett tal: 7
# 7777777
# Om talet är 5 eller mindre: En rad med varje sådan sträng som ovan upp till och med talet. Till exempel:
# Ange ett tal: 4
# 1
# 22
# 333
# 4444


# my_value = 7 #input("skriv en integer: ")

# if int(my_value) > 5:
#     my_value = str(my_value) * int(my_value)
#     print(my_value)
# else:
#     for i in range(1, int(my_value)+1):
#         my_value = str(i) * int(i)
#         print(my_value)

# Skapa en ny version som använder sig av funktioner.
def my_numbers(my_value):
    if int(my_value) > 5:
        my_value = str(my_value) * int(my_value)
        print(my_value)
    else:
        for i in range(1, int(my_value)+1):
            my_value = str(i) * int(i)
            print(my_value)

#my_numbers(input("Skriv integer till: "))

my_int = 7 #input("Skriv ett tal: ")
if int(my_int) < 5:
    for i in range(int(my_int)):
        str_num = str(i) 
        str_num = str_num * i 
        print(str_num)
else:
    str_num = str(my_int)
    str_num =  str_num * int(my_int)
    print(str_num)