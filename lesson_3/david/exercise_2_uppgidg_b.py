# person 1 information
from ast import Compare
from gettext import find


person_1_name = "kalle".title() #input("Please enter name for person 1: ").title()
person_1_age = 55 #input("Please enter age for person 1: ")
person_1_shoe_size = 19 #input("Please enter shoe size for person 1: ")

# person 2 information
person_2_name = "anders".title() #input("Please enter name for person 2: ")
person_2_age = 77 #input("Please enter age for person 2: ")
person_2_shoe_size = 14 #input("Please enter shoe size for person 2: ")

# person 3 information
person_3_name = "max".title() #input("Please enter name for person 3: ")
person_3_age = 66 #input("Please enter age for person 3: ")
person_3_shoe_size =  34 #input("Please enter shoe size for person 3: ")

#lägg till personer i en dictionary. namn är key age och shoe size är väredn.
"""
person_1 = {person_1_name : (person_1_age, person_1_shoe_size)}
print(person_1)

person_2 = {person_2_name : (person_2_age, person_2_shoe_size)}
print(person_2)

person_3 = {person_3_name : (person_3_age, person_3_shoe_size)}
print(person_3)

"""

"""
persons_all = {person_1_name : (person_1_age, person_1_shoe_size),
person_2_name : (person_2_age, person_2_shoe_size),
person_3_name : (person_3_age, person_3_shoe_size)  }
print(persons_all)
"""

persons = [(person_1_name, person_1_age, person_1_shoe_size),
(person_2_name, person_2_age, person_2_shoe_size), 
(person_3_name, person_3_age,person_3_shoe_size)]

print(persons)

#skriva ut namn och skostorlek på den person som är äldst
#oldest_person = sorted(persons_all.values(), key=lambda y: y[0])[-1]
#print(oldest_person)
#sorterar persons på andra positionen(person_X_age) och [-1] väljer positionen (första bakifrån) att spara i variabeln.
#oldest = list(persons)
oldest = sorted(persons, key=lambda old: old [1])[-1]
#skriver ut värdet i oldest på position 0 och sedan värdet i oldest på position 2.
print(f"The oldest person is {oldest[0]} who has shoe size {oldest[2]}. ")

#my_dict = {v: k for k, v in my_dict.items()}

#namn och ålder på den som har medianskostorlek
#sorterar persons på tredje positionen[2](person_X_shoe_size) och [1] väljer positionen (den mittersta) att spara i variabeln.
medianstorlek_shoe = sorted(persons, key=lambda medianstorlek: medianstorlek [2])[1]
#print(persons)
#print(medianstorlek_shoe)
print(f"The person with median shoe size is {medianstorlek_shoe[0]} who is {medianstorlek_shoe[1]} years old. ")

#print(f"The oldest person is {oldest_person} who has shoe size {} ")

hitta = input("Please enter search value, name, age or size followed by value. ")
print(hitta)
name = persons[0]
print(name)
age = persons[1]
print(age)
shoe_size = persons[2]
print(shoe_size)

#print(f" hitta {sök in persons} ")