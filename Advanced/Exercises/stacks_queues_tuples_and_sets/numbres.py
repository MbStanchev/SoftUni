line_1 = set([int(x) for x in input().split()])
line_2 = set([int(y) for y in input().split()])

num_of_commands = int(input())

for i in range(num_of_commands):
    commands = input().split()
    operation = commands[0]
    num_of_line = commands[1]

    sequence = [(int(x)) for x in commands[2:]]

    if operation == 'Add' and num_of_line == 'First':
        line_1.update(sequence)

    elif operation == 'Add' and num_of_line == 'Second':
        line_2.update(sequence)

    elif operation == 'Remove' and num_of_line == 'First':
        line_1 = line_1.difference(sequence)

    elif operation == 'Remove' and num_of_line == 'Second':
        line_2 = line_2.difference(sequence)

    elif operation == 'Check':
        if line_2.issubset(line_1) or line_1.issubset(line_2):
            print('True')
        else:
            print('False')

print(*sorted(line_1), sep=', ')
print(*sorted(line_2), sep=', ')
