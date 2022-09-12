import string

alphabet_list = list(string.ascii_lowercase)
print(alphabet_list)

stack = []
for i in alphabet_list:
    stack.append(i)
print(stack)

alphabet_str =""
for i in range(len(stack)):
    alphabet_str =  alphabet_str + stack.pop() + " "

print(alphabet_str)