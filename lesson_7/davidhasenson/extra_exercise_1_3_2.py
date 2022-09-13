def my_number(number):
    num_string = str(number)
    num_string = num_string * number
    print(num_string)
#my_number(5)

my_int = 4 #input("Skriv ett tal: ")
if int(my_int) < 5:
    for i in range(1, int(my_int)+1):
        my_number(i)
else:
    my_number(my_int)