firstname = "john"
lastname = "smith"
tele = "00468123456789"

# Print first, lastname and tele on the same line
print(firstname, lastname, tele)
print(firstname, end=" ")
print(lastname, end=" ")
print(tele)

# Create a variable fullname
# Assign to the new variable fullname, firstname and lastname separated with a space.
fullname = firstname+" "+lastname
#print(fullname)

# Print the lenght len() of fullname, firstname and lastname
print(len(fullname))
print(len(firstname))
print(len(lastname))

# Print a escape sequence \n so the first line contains fullname, and the second line tele.
print(f"{fullname}\n{tele}")

# Write the fullname and tele with the four different methods:
# Only using print() and string concatenation i.e "firstname" + " " ..
print(firstname+" "+lastname+" "+tele)
# Using f-string
print(f"{firstname} {lastname} {tele}")
# Using format, i.e print('{}'.format(firstname))
print("{} {} {}".format(firstname, lastname, tele))
# Using printf (%) syntax, i.e print('A name %s' % firstname)
print(f"A name %s %s %s" %(firstname, lastname, tele))