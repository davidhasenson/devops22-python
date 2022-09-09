# Skriv ett program som tar emot två strängar från användaren
string_1 = "Första ströngen" #input("Skriv någonting. ")
string_2 = "Andra strängen" #input("Skriv mer. ")
# Lägg till enkla citationstecken i början och slutet av den första strängen, till exempel så här:
# new_first_string = "'" + first_string + "'"
new_string_1 = "'"+string_1+"'"
# Lägg till dubbla citationstecken i början och slutet av den andra strängen
New_string_2 = '"'+string_2+'"'
# Lägg ihop första och andra strängen med tecknet för ny rad mellan.
combine_strings = new_string_1 + "\n" + New_string_2
# Skriv ut den nya strängen som svar.
print(combine_strings)

# Testa dig igenom alla escape-sekvenser nämnda i presentationen genom en
# serie print-kommandon. (Teckenkoder för att testa de escapesekvenserna
# kan du exempelvis hitta här: https://www.fileformat.info/info/unicode/block/miscellaneous_symbols/). 
# För att se resultatet bör du ha ett tecken före och ett tecken efter, exempelvis:
# print("A\nB")

print("[1] a\\b")
print("[2] a\'b")
print("[3] a\"b")
print("[4] a\ab")
print("[5] a\bb")
print("[6] a\fb")
print("[7] a\nb")
print("[8] a\rb")
print("[9] a\tb")
print("[10] a\vb")
print("[11] a\000b")
#print("[12] a\xhhb")
