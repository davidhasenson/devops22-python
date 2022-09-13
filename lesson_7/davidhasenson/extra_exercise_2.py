my_int = 7 #input("Skriv ett tal: ")
if int(my_int) < 5:
    for i in range(int(my_int)):
        str_num = str(i) 
        str_num = str_num * i 
        print(f" svar: {str_num}")
else:
    str_num = str(my_int)
    str_num =  str_num * int(my_int)
    print(f"Svar: {str_num}")



def my_number(number):
    num_string = str(number)
    num_string = num_string * number
    print(f"svar: {num_string}")
#my_number(5)

my_int = 4 #input("Skriv ett tal: ")
if int(my_int) < 5:
    for i in range(1, int(my_int)+1):
        my_number(i)
else:
    my_number(my_int)