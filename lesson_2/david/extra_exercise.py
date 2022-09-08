# 1
A = 5
B = A
A = 7
C = A+B
print (C)

#2
A = 7 * 3 +1
print(A)

#3
A = 20/4*2
print(A)

A = 20/(4*2)
print(A)

#4
A = 1
B = A
A = A + B
B = A + B
C = A + B
print(C)

#5
print("Hello World")

#6
tal_A = int(input("Skriv ett tal: "))
tal_B = int(input("Skriv ett tal till: "))
print(tal_A+tal_B)
print(tal_A-tal_B)
print(tal_A*tal_B)

#7
tal_C = float(input("Skriv tal ett: "))
tal_D = float(input("Skriv tal två: "))
print(f"{tal_C} delat på {tal_D} blir {tal_C/tal_D}")
print(f"{tal_D} delat på {tal_C} blir {tal_D/tal_C}")

#Vad är uppgiften?
print(f"{tal_C} delat på {tal_D} som integer blir {int(tal_C)/int(tal_D)}")
print(f"{tal_D} delat på {tal_C} som integer blir {int(tal_D)/int(tal_C)}")

#8 
from math import pi
from urllib.parse import SplitResult

# Skriv in ett värde på cirkelns radie.
radie = float(input("Skriv in cirkelns radie så får du veta dess area:"))
#Beräknar arean.
area = pi*(radie**2)
# Skriver ut arean.
print(area)

#9
print("Beräkna arean av en triangel.")
triangel_bas = float(input("Skriv in triangelns bas: "))
triangel_höjd = float(input("Skriv in triangelna höjd: "))
# Beräkna arean
area = (triangel_bas*triangel_höjd)/2
# Skriv ut resultatet.
print(f"Arean på triangeln är {area}")

#10 
# Vad är uppgiften?
# x = float(input("Skriv ett nummer :"))
# y = float(input("Skriv ett nummer till:"))
# resultat = (x+y)*(x+y)
# print(resultat)

#11

from math import sqrt

print("Beräkna hypotenusan i en rätsidig triangel.")
katet = float(input("Skriv längden på katetern: "))
# Beräkna hypotenusan i rätvinklig triangel
hypotenusa = sqrt((katet**2)+(katet**2))
print(f"Hypotenusan är {hypotenusa} lång. ")

#12

tid = 455
timmar = tid//60
# Är det här rätt. Vad händer här?
minuter = tid%60
print(f"Det är {timmar} timmar och {minuter} minuter på 455 minuter. ")

#13
# Hjälp
tid = float(input("Skriv ett antal sekunder så får du veta hur många dagar, timmar, minuter och sekunder det går på de sekunderna. "))
dagar = int(tid//86440)
timmar = int(tid//3600)
minuter = int(tid//60)
sekunder = int(tid%60)
print(f"Det är dagar {dagar}, timmar {timmar}, minuter {minuter} och sekunder {sekunder} på {tid} sekunder. ")