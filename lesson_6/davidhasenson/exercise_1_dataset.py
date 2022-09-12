
# Generate a list containing the numbers 1, 2, 3 to 100.
import random
from random import choices


one_to_hundred = [x for x in range(1, 101)]
#print(one_to_hundred)
# Generate a list of all even numbers from 2 to 60
one_to_hundred_even = [x for x in range(1, 61) if x % 2 == 0]
#print(one_to_hundred_even)
# Generate a list of all odd numbers from 1 to 77
one_to_hundred_odd =[x for x in range(1, 78) if x % 2 != 0]
#print(one_to_hundred_odd)
one_to_hundred_random_unique = random.sample(range(1, 301), 100)
#print(sorted(one_to_hundred_random_unique))
one_to_hundred_random_not_unique = random.choices(range(1, 301), k=100)
#print(sorted(one_to_hundred_random_not_unique))
coloe_list = ["orange", "Green", "Yellow", "Blue", "black"]
my_colors = ["Red"]
random_collor = choices(coloe_list, k=2)
#print(random_collor)
my_colors = my_colors + random_collor
#print(my_colors)
fifty_random_colors = choices(random_collor, k=50)
#print(fifty_random_colors)
random_collor_set = set(random_collor)
coloe_set = set(coloe_list)
my_colors_set = set(my_colors)
fifty_random_colors_set = set(fifty_random_colors)
print(f"Lista 1 längd {len(coloe_list)} unika {len(coloe_set)} {coloe_set} ")
print(f"Lista 2 längd {len(my_colors)} unika {len(my_colors_set)} {my_colors_set} ")
print(f"Lista 3 längd {len(fifty_random_colors)} unika {len(fifty_random_colors_set)} {fifty_random_colors_set}")
