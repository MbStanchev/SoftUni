list_of_coffies = input().split()
num_of_commands = int(input())

for i in range(num_of_commands):
    commanda = input().split()

    if commanda[0] == 'Include':
        list_of_coffies.append(commanda[1])
        continue

    elif commanda[0] == 'Remove':
        if int(commanda[2]) > len(list_of_coffies):
            continue
        if commanda[1] == 'first':
            for j in range(0, int(commanda[2])):
                list_of_coffies.pop(0)

        elif commanda[1] == 'last':
            for j in range(len(list_of_coffies), len(list_of_coffies) - int(commanda[2]), -1):
                list_of_coffies.pop(-1)
        continue

    if commanda[0] == 'Prefer':
        if 0 <= int(commanda[1]) <= len(list_of_coffies) and 0 <= int(commanda[2]) <= len(list_of_coffies):
            list_of_coffies[int(commanda[1])], list_of_coffies[int(commanda[2])] = list_of_coffies[int(commanda[2])], list_of_coffies[int(commanda[1])]
            continue
        else:
            continue

    if commanda[0] == 'Reverse':
        list_of_coffies.reverse()
        continue
print('Coffees:')
print(' '.join(list_of_coffies))
