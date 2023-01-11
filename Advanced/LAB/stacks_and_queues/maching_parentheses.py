entry = input()
stack = []
# for simvol in entry:
#     if simvol == '(':
#       stack.append(entry.index(simvol))
# print(stack)
for index in range(len(entry)):
    if entry[index] == '(':
       stack.append(index)

    elif entry[index] == ')':
        start_index = stack.pop()
        print(entry[start_index: index + 1])