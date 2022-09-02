# person 1 information
person_1_name = "kalle" #input("Please enter name for person 1: ").title()
person_1_age = 55 #input("Please enter age for person 1: ")
person_1_shoe_size = 9 #input("Please enter shoe size for person 1: ")

# person 2 information
person_2_name = "hej" #input("Please enter name for person 2: ")
person_2_age = 77 #input("Please enter age for person 2: ")
person_2_shoe_size = 14 #input("Please enter shoe size for person 2: ")

# person 3 information
person_3_name = "max" #input("Please enter name for person 3: ")
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
persons_all = {person_1_name : (person_1_age, person_1_shoe_size),
person_2_name : (person_2_age, person_2_shoe_size),
person_3_name : (person_3_age, person_3_shoe_size)  }

print(persons_all)

#skriva ut namn och skostorlek på den person som är äldst
oldest_person = sorted(persons_all.values(), key=lambda y: y[0])[-1]

print(oldest_person)

#my_dict = {v: k for k, v in my_dict.items()}

#namn och ålder på den som har medianskostorlek
#medianstorlek_shoe = 

#print(f"The oldest person is {oldest_person} who has shoe size {} ")