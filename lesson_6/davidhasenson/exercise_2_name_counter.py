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
print(top_name)

least_popular_name = Counter(name_list).most_common(3)[:-3-1:-1]
print(least_popular_name)

sorted_names = sorted(count_name)
print(set(count_name))


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