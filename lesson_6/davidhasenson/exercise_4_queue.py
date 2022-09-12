from collections import deque
import random

# Generate a list with 50 names
name_list = random.choices(["johan", "lisa", "jonas", "tove", "max", "karin", "adam"], k=50)

# Create a Queue deque with a maximum length of 10
name_queue = deque(name_list, maxlen=10)

for x in range(random.randint(0, len(name_queue))):
    name_queue.pop()

for x in range(name_queue.maxlen-len(name_queue)):
    name_queue.append(random.choice(name_list))

i = 0
for x in name_list:
    name_queue.popleft()
    print(f"pop {name_queue}  {len(name_queue)}")
    name_queue.append(name_list[i])
    i +=1
    print(f"append {name_queue} {len(name_queue)} ")