# Genom att använda en for-loop, skriv ett program som för varje tal i second_list, hämtar
# talet och dess position i first_list och skriver resultatet som en lista av tupler.
# Exempel:
# first_list = [3, 7, 9, 2, 6]
# second_list = [2, 3, 6, 7, 9]
# Output: [(2, 3), (3, 0), (6, 4), (7, 1), (9, 2)]

from gettext import find


first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]
new_list = []


for x in second_list:
   if x == first_list:
    print(x)
    new_list.append(x ,y)
   
print(new_list)
   
   
"""" for y in second_list:
        a = (x, y)
        combined_list.append(a)
   #     y =+1
  #      z =+1
        #print(x, y )
     
        break
print(combined_list)
"""