from operator import itemgetter

persons = []

# person 1 information
person_1_name = "kalle".title() #input("Please enter name for person 1: ").lower()
person_1_age = 55 #int(input("Please enter age for person 1: "))
person_1_shoe_size = 19 #float(input("Please enter shoe size for person 1: "))
person_1 = (person_1_name, person_1_age, person_1_shoe_size)
persons.append(person_1)

# person 2 information
person_2_name = "anders".title() #input("Please enter name for person 2: ").lower()
person_2_age = 77 #int(input("Please enter age for person 2: "))
person_2_shoe_size = 14 #float(input("Please enter shoe size for person 2: "))
person_2 = (person_2_name, person_2_age, person_2_shoe_size)
persons.append(person_2)

# person 3 information
person_3_name = "max".title() #input("Please enter name for person 3: ").lwer()
person_3_age = 66 #int(input("Please enter age for person 3: "))
person_3_shoe_size =  34 #float(input("Please enter shoe size for person 3: "))
person_3 = (person_3_name, person_3_age, person_3_shoe_size)
persons.append(person_3)

# sortera på ålder
sort_age = sorted(persons, key=itemgetter(1))
# sortera på skostorlek
sort_shoe_size = sorted(persons, key=itemgetter(2))
# spara den sista i listan i variabeln
oldest = sort_age[-1]
# spara den på plats 1 i listan i variabeln
median_shoe_size = sort_shoe_size[1]

#skriva ut namn och skostorlek på den person som är äldst
print(f"The oldest person is {oldest[0].capitalize()} who has shoe size {oldest[2]}")
# skriv ut den person som har medianskostorlek
print(f"The person with median shoe size is {median_shoe_size[0].capitalize()} who is {median_shoe_size[1]} years old.")

searches = {
    "age": {
        str(person_1_age): person_1,
        str(person_2_age): person_2,
        str(person_3_age): person_3
    },
    "shoe": {
        str(person_1_shoe_size): person_1,
        str(person_2_shoe_size): person_2,
        str(person_3_shoe_size): person_3
    },
    "name":{
        str(person_1_name): person_1,
        str(person_2_name): person_2,
        str(person_3_name): person_3
    }
}

prop, value = input("Enter prop value: ").split(" ")
print(searches[prop][value])