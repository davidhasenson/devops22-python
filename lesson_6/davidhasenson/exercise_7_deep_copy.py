from copy import copy, deepcopy


name_list = ["johan", "lisa", "jonas", "tove", "max", "karin", "adam"]
name_list_copy = copy(name_list)
name_list_deepcopy = deepcopy(name_list)

name_list.pop()
name_list.append("Anna")

print(f"list {name_list} ")
print(f"list copy {name_list_copy} ")
print(f"list deepcopy {name_list_deepcopy} ")

