# Skapa ett program som frågar efter två tal och skriver ut summan, differensen,
# produkten och kvoten av talen.

from difflib import diff_bytes


tal_1 = 100 #int(input("Skriv ett tal. "))
tal_2 = 10 #int(input("Skriv ett tal. "))
summa = tal_1 + tal_2
print(summa)
differens = tal_1 - tal_2
print(differens)
produkt = tal_1 * tal_2
print(produkt)
kvot = tal_1 / tal_2
print(kvot)

# Presentationen av resultaten för de olika räknesätten ska använda sig av
# olika metoder för stränginterpolation, det vill säga:
# (a) Strängkonkatenering
print(str(summa) + " " + str(differens))
#print(" ".join([summa, differens]))
# (b) %-operatorn
print("%d %d"%(summa, differens))
# (c) .format-sträng
print("{} {}".format(summa, differens))
# (d) f-sträng
print(f"{summa} {differens}")