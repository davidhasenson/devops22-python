from collections import deque
import random

name_list = random.choices(["johan", "lisa", "jonas", "tove", "max", "karin", "adam"], k=50)
name_queue = deque(name_list)
print(name_queue)