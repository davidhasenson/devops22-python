import random
from typing import Counter


name_list = random.choices(["johan", "lisa", "jonas", "tove", "max", "karin", "adam"], k=100)
print(len(name_list))


count_name = {}
for name in name_list:
    if name in count_name:
        count_name[name] += 1
    else:
        count_name[name] = 1
print(count_name)


top_name = Counter(name_list).most_common(3)
print(f"Top names {top_name} ")

least_popular_name = Counter(name_list).most_common(3)[::-1]
print(f"Least popular names {least_popular_name} ")

sorted_names = sorted(set(count_name))
print(sorted_names)

sorted_names_shuffled = random.shuffle(sorted_names)
print(sorted_names_shuffled)

sorted_names_reverse = sorted_names[::-1]
print(sorted_names_reverse)

"""

c = Counter(count_name)
print(c.most_common()[:3])
print(c.most_common()[::-1])

sorted_count_name = sorted(count_name)
print(sorted_count_name)
random.shuffle(sorted_count_name)
print(sorted_count_name)
sorted_count_name = sorted(count_name)
print(sorted_count_name[::-1])
"""