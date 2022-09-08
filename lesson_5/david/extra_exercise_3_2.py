# Skriv ett program som börjar med strängen "Jag tYcker om äGg" och i
# slutändan skriver ut strängen "jAG tYCKER iNTE oM SPAM"
# Följande strängar är de enda som får hårdkodas:
# (a) "Jag tYcker om äGg"
# (b) "inte"
# (c) "SPAM"
# (d) " " (Alltså ett mellanslag)

# Programmet ska inte ta någon användarinput
# Följande strängmetoder får användas:
# (a) capitalize()  Converts the first character to upper case
# (b) join()        Joins the elements of an iterable to the end of the string
# (c) lower()       Converts a string into lower case
# (d) upper()       Converts a string into upper case
# (e) swapcase()    Swaps cases, lower case becomes upper case and vice versa
# (f) replace()     Returns a string where a specified value is replaced with a specified value
# (g) split()       Splits the string at the specified separator, and returns a list
# (h) rsplit()      Splits the string at the specified separator, and returns a list
# (i) title()       Converts the first character of each word to upper case
# (j) format()      Formats specified values in a string

# Programmet ska skriva ut vad som gjorts samt hur strängen ser ut efter varje genomförd rad.


ny_str = "Jag tYcker om äGg"
inte_str = "inte"
spam_str = "SPAM"
mellanslag_str = " "

print(f"Startar med en mening som ser ut så här: \"{ny_str}\" ")

ny_str = ny_str.lower()
print(f"Ändrat alla bokstäver till gemener med .liwer(). Resultatet blir \"{ny_str}\" ")

word_list = ny_str.split()
print(f"Dela upp strängen i en lista med .split() där varje ord är ett listobjekt \"{word_list}\" ")

word_list.insert(2, inte_str)
print(f"Lägger till \"inte\" i listan med .insert() Resultatet blir \"{word_list}\" ")

ny_str = mellanslag_str.join(word_list)
print(f"Skapar en sträng med .join() från listan med mellanslag mellan varje listobjekt. Resultatet blir \"{ny_str}\" ")

#ny_str = ny_str.replace("ägg", spam_str)
#print(f"Byter ut ägg mot spam med .replace. Resultatet blir \"{ny_str}\" ")

ny_str = ny_str.title()
print(f"Konverterar det första tecknet i varje ord till versaler och resten till gemener med .title(). Resultatet blir \"{ny_str}\" ")

ny_str = ny_str.swapcase()
print(f"Byter ut alla gemener mot versaler och vice verse. Resultatet blir \"{ny_str}\" ")

ny_str = ny_str.replace("äGG", spam_str)
print(f"Byter ut äGG mot spam med .replace. Resultatet blir \"{ny_str}\" ")


