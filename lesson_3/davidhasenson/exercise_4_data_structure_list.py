# 1 Create a empty list
color_list_1 = []

# 2 Create a string that is a color e.g "red"
color = str("red")

# 3 Add the color to your list
color_list_1.append(color)

# 4 Print the color from the list using Common Sequence Operations indexing for 0 i.e my_list[0]
print(color_list_1[0])

# 5 Add two other color to the list
color_list_1.append("green")
color_list_1.append("blue")
print(color_list_1)

# 6 Search for a color in the list using operation x in s
find_color =  "red" #input("Write a clor:")
print(find_color in color_list_1)

# 7 Verify that a color is not in the list using the operation x not in s
find_color = "yellow"
print(find_color not in color_list_1)

# 8 Create another list of colors and concatenate the two lists using the operation s + t
color_list_2 = ["yellow", "oange", "pink"]
color_list_1 = color_list_1 + color_list_2
print(color_list_1)

# 9 Create a list of two colors red, yellow with three of each color using the operation s * n
color_list_3 = ["red", "yellow"]
color_list_3 = color_list_3 * 3
print(color_list_3)

# 10 Print the first four colors in the list from (9) using the operation s[i:j]
print(color_list_3[0:4])

# 11 Count how many times "red" occur in the list using the operation s.count(x)
count_color = color_list_3.count("red")
print(count_color)

# 12 Print the index of the first occurrence of "yellow" in s using the operation s.index("yellow")
index_color = color_list_3.index("yellow")
print(index_color)

# 13 Print the total length of each array using the operation len(s)
arrey_lenght = len(color_list_3)
print(arrey_lenght)

# 14 Create a list of 7 numbers
number_list = [5, 1, 3, 4, 7, 6, 2]
print(number_list)

#Print the min value in the list
sorted_numbers = sorted(number_list)
print(sorted_numbers[0])

#Print the max value in the list
sorted_numbers = sorted(number_list)
print(sorted_numbers[-1])
# eller så här
print(sorted(number_list)[-1])