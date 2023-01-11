entry = input()
str_as_stack = []
for i in entry:
    str_as_stack.append(i)
while len(str_as_stack) > 0:
    print(str_as_stack.pop(), end='')