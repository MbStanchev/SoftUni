n = int(input())
matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
while True:
    command = input().split()
    if command[0] == 'END':
        break
    command, r, c, value = command[0], int(command[1]), int(command[2]), int(command[3])
    if not (0 <= r < n and 0 <= c < n):
        print('Invalid coordinates')
        continue
    if command == "Add":
        matrix[r][c] += value
    elif command == "Subtract":
        matrix[r][c] -= value

for i in matrix:

    print(*i)
