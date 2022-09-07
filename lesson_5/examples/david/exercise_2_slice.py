firstname = "john"
lastname = "smith"
tele = "00468123456789"
fullname = firstname+" "+lastname

# Use slice to get the first 5 characters i fullname
print(fullname[:5])
# Use slice to get all characters except the first and last one
print(fullname[1:-1])
# Use slice to get every other character, i.e abcdef would print ace. Print the result in uppercase.
print(fullname.upper()[::2]+" "+tele.upper()[::2])
# Use slice to print a word backwards.
print("Hello"[::-1])
# Use slice to get the 5th character
print("Hello"[4])