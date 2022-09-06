# Skriv ett program som loopar över en lista innehållandes olika tal. Om programmet stöter
# på ett ojämnt tal skrivs orden “Not allowed!” ut och loopen avbryts.

my_list = [2, 4, 6, 8, 10,]

for x in my_list:
    if x %2 != 0:   
        print("Not allowed!") 
        break