def validate_int(my_input):
    try: 
        #return int(input(my_input))
        my_int = int(input(my_input))
        if my_int % 2 == 0:
            raise  Exception('Even numbers is not allowed')
        return my_int
    except ValueError:
        print("Sorry, not an int")
        return validate_int(my_input)
        

my_number = validate_int("skriv en integer ")
print(my_number)