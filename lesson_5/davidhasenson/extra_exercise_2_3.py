# Låt användaren skriva in tal genom att använda input(). Se till att skriva
# en begriplig uppmaning till användaren.
tal_1 = 100 #input("Srin inett tal. ")
tal_2 = 10 #input("Skriv in ett till tal. ")
# Gör beräkningar av summa, dfferens, produkt och kvot. För att kunna det
# behöver du konvertera strängarna till tal genom att använda funktionen int.
tal_1 = int(tal_1)
tal_2 = int(tal_2)

summa = tal_1 + tal_2
print(summa)
differens = tal_1 - tal_2
print(differens)
produkt = tal_1 * tal_2
print(produkt)
kvot = tal_1 / tal_2
print(kvot)

# Gör strängar av typen "Summan av [tal] och [tal] är [resultat] där programmet
# lagt in rätt värden genom metoderna som beskrivs ovan.
str_summa = (f"Summan av {tal_1} och {tal_2} är {summa}")
str_differens = (f"Differencen av {tal_1} och {tal_2} är {differens}")
str_produkt = (f"Produkten av {tal_1} och {tal_2} är {produkt}")
str_kvot = (f"Kvoten av {tal_1} och {tal_2} är {kvot}")

#Skriv ut strängarna
print(str_summa)
print(str_differens)
print(str_produkt)
print(str_kvot)