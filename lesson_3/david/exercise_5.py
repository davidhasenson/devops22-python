#Exercise 5 Sorting
# In LINKS_3.md there is a link Python guide how-to do sorting. Create a list containing 10 car brand. i.e cars = ["volvo", ...]
from audioop import reverse
from operator import itemgetter


cars =["volvo", "saab", "bmw", "tesla", "ford", "audi","toyota", "subaru", "nissan", "kia"]

# Sort the list with sorted(cars)
sorted_cars = sorted(cars)
print(sorted_cars)

# Sort the list with cars.sort()
sorted_cars = cars.sort()
print(sorted_cars)

# reverse the sort of both, read more about reversing in python docs ascending-and-descending
sorted_cars = sorted(cars, reverse=True) 
print(sorted_cars)

sorted_cars = cars.sort(reverse=True)
print(sorted_cars)

# Extra exercise, create a list of 10 tuples containing (brand, model), i.e ("volvo", "xc90"). Sort first on brand, then on model.
car_tuple = [("volvo", "xc90"), ("saab", "saab 9-3"), ("audi", "q5"),("tesla", "model s"),("volvo", "xc70"), ("toyota", "rav4"),]
sorted_cars = sorted(car_tuple, key=itemgetter(0,1))
print(sorted_cars)