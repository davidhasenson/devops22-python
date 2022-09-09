# 1 Vad blir då värdet på C? Vad trodde du att det skulle bli?
A = 5       # A får värdet 5.
B = A       # B får samma värde som A har. B har värdet 5.
A = 7       # A får ett nytt värde. A har värdet 7.
C = A+B     # C får värdet som A har plus värdet som B har. A(7) + B(5) = 12. C får värdet 12. 
print (C)   # Skriver ut värdet för C som är 12.

# 2 Vad blir värdet på A?
A = 7 * 3 +1    # Multiplikation går före addition
print(A)        # Skriver ut 22

# 3 Vad blir A? Vad kan man göra för att slippa missförstånd kring vad A blir?
A = 20/4*2      # Läser från vänster till höger. Använd parenteser för att förtydliga.
print(A)        # Skriver ut 10

A = (20/4)*2
print(A)

# 4 Vad blir värdet på C?
A = 1
B = A           # B = 1
A = A + B       # A = 1 + 1
B = A + B       # B = 2 + 1
C = A + B       # C = 2 + 3
print(C)        # Skriver ut 5

# 5 Använd python för att skriva “Hello World” till skärmen
print("Hello World")

# 6 Skriv ett program som först ber användaren om tal A, sedan tal B
tal_A = input("Skriv ett tal: ")
tal_B = input("Skriv ett tal till: ")
# Men båda är nu strängar. Konvertera till int:
tal_A_int = int(tal_A)
tal_B_int = int(tal_B)
# Skriv ut summan av de båda talen
print(tal_A_int+tal_B_int)
# Skriv ut skillnaden mellan de båda talen
print(tal_A_int-tal_B_int)
# Skriv ut de båda talen multiplicerade med varandra.
print(tal_A_int*tal_B_int)

# 7 Ta in två tal från användaren som i uppgiften ovan och:
tal_A = input("Skriv tal ett: ")
tal_B = input("Skriv tal två: ")
# Konvertera till int
tal_A_int = int(tal_A)
tal_B_int = int(tal_B)
# Använd division för att se vad de olika talen blir delat på varandra, skriv resultatet till skärm.
print(f"{tal_A_int} delat på {tal_B_int} blir {tal_A_int/tal_B_int}")
# Använd heltalsdivision för att se vad de olika talen blir delat på varandra, skriv resultatet till skärm.
print(f"{tal_A_int} delat på {tal_A_int} som integer blir {tal_A_int//tal_B_int}")

# 8 Skriv ett program som tar in radien på en cirkel från användaren och beräknar cirkelns area

# Vägledning: Ni måste skriva from math import pi i ert program för att kunna använda ett
# mycket exakt pi i beräkningarna. Om ni inte bryr er om att vara exakta går det bra att
# bara sätta pi till 3,14
from math import pi

# Skriv in ett värde på cirkelns radie.
radius = int(input("Skriv in cirkelns radie så får du veta dess area:"))
#Beräknar arean.
area = pi*radius**2
# Skriver ut arean.
print(f"Arern är {area}")

# 9 Skriv ett program som tar höjden och basen på en triangel som input, och utifrån det
# beräknar triangels area
print("Beräkna arean av en triangel.")
triangel_bas = int(input("Skriv in triangelns bas: "))
triangel_höjd = int(input("Skriv in triangelna höjd: "))
# Beräkna arean
area = (triangel_bas*triangel_höjd)/2
# Skriv ut resultatet.
print(f"Arean på triangeln är {area}")

# 10 Skriv ett program som löser ekvationen (x+y)*(x+y)
x = 2 
y = 3 
resultat = x**2+2*x*y+y**2
print(f"(x+y)*(x+y) x=2 y=3 blir {resultat}")

# 11 Skriv ett program som räknar ut hypotenusan I en rätsidig triangel
# Vägledning: Ni behöver skriva in from math import sqrt i källkodsfilen
from math import sqrt

print("Beräkna hypotenusan i en rätsidig triangel.")
base = int(input("Skriv längden på basen: "))
hight = int(input("Skriv längden på höjden:"))
# Beräkna hypotenusan i rätvinklig triangel
hypotenusa = sqrt((base**2)+(hight**2))
print(f"Hypotenusan är {hypotenusa} lång. ")

# 12 Skriv ett program som räknar ut antalet timmar och minuter det går på 455 minuter.
total_number_of_minutes = 455
number_of_houer = total_number_of_minutes//60
number_of_minutes = total_number_of_minutes%60
print(f"Det är {number_of_houer} timmar och {number_of_minutes} minuter på 455 minuter. ")

# 13 Skriv ett program som ber användaren att skriva in ett antal sekunder och sedan räknar
# ut hur många dagar, timmar, minuter och sekunder det går på de sekunderna.
total_seconds = int(input("Skriv ett antal sekunder så får du veta hur många dagar, timmar, minuter och sekunder det går på de sekunderna. "))
# Beräkna antal dagar
seconds_in_a_day = 60*60*24
number_of_days = total_seconds//seconds_in_a_day
print(number_of_days)
# Beräkna antal timmar
seconds = total_seconds%seconds_in_a_day
seconds_in_an_hour = 60*60
number_of_houers = seconds//seconds_in_an_hour
print(number_of_houer)
# Beräkna sekunder
seconds = seconds%seconds_in_an_hour
print(seconds)

# 14 a = okänt variabel b = okänt variabel. (Vilka som helst, integer, float eller string som du
# sätter själv) a få samma värde som b och b samma som a :
# Skriv koden som gör det som står på raden ovan. Använd gärna hjälp variabel “c” för att klara uppgiften.
a = "Hello"
b = "World"
c = a
a = b
b = c
print(a)
print(b)
# Skriv koden som gör det utan att använda någon hjälpvariabel.
a, b = b, a
print(a)
print(b)

# 15 Använd multipel tilldelning för att ge x, y, z samma värde
x = y = z = "Hello World"
print(x)
print(y)
print(z)

# 16 Be användaren att skriva in olika temperaturer, konvertera sedan temperaturen till 
# fahrenheit Fahrenheit = Celsius * 9/5 + 32
celcius = float(input("Skriv en temperatur: "))
fahrenheit = celcius * (9/5) + 32
print(f"{celcius} Celcius är {fahrenheit} Fahrenheit")

# 17
# 18
# 19