ny_str = "jAg tYcker om äGg"

# ny_str.capitalize utförs men sparas ingenstans. 
# Print skriver ut en omodifieras sträng.
ny_str.capitalize()
print(ny_str)

# Strängen modifieras och resultater skrivs ut.
# Modifieringen sker bara för den utskriften ingen annan stans.
print(ny_str.capitalize())

# Modifieringen skaras i en variabel och variabeln skrivs ut.
ny_str = ny_str.capitalize()
print(ny_str)