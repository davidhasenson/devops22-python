# Genom att använda en for-loop, skriv ett program som för varje tal i second_list, hämtar
# talet och dess position i first_list och skriver resultatet som en lista av tupler.
# Exempel:
# first_list = [3, 7, 9, 2, 6]
# second_list = [2, 3, 6, 7, 9]
# Output: [(2, 3), (3, 0), (6, 4), (7, 1), (9, 2)]

first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]
new_list = []
# print(second_list[1])
# print(second_list.index(3))

# om x är mindre än längden listan utför loopen
for x in range(len(second_list)):
   #print(x)
   # om värdet i second_list[x] finns i first_list. gå in.
   if second_list[x] in first_list: 
        # print(second_list[x]) 
        # print(first_list[x])
        
        # second_list[x] hämtar värdet på position x i second_list. 
        # first_list.index() hämtar index (platsen i en lista) i first_list för värdet som gavs av second_list[x] 
        # first_list[] hämtar värdet som finns på index (platsen) som first_list.index() anger
        get_index = first_list[first_list.index(second_list[x])]
        # .index breättar positionen i first_list på värdet som anges av second_list[x] ?
        #eller
        # second_list[x] hämtar värdet på position x i second_list. 
        # first_list.index() hämtar index (positionen i en lista) i first_list för värdet som gavs av second_list[x]
        get_value = first_list.index(second_list[x])
        # print(get_index)
        # print(get_value)

        # skapa en ny tuple med värdena
        new_tuple = (get_index, get_value)
        # print(new_tuple)

        # lägg till puple til lista
        new_list.append(new_tuple)
print(new_list)