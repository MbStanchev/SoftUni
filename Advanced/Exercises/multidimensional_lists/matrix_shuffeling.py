rows, cols = [int(x) for x in input().split()]
matrix = []

for i in range(rows):
    matrix.append([x for x in input().split()])

entry = input()
while entry != 'END':
    command = entry.split()
    if command[0] != 'swap' or len(command) != 5:
        print("Invalid input!")
        entry = input()
        continue
    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if row1 > rows or col1 > cols or row2 > rows or col2 > cols or \
            row1 < 0 or col1 < 0 or row2 < 0 or col2 < 0:
        print("Invalid input!")
        entry = input()
        continue
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    entry = input()
    for row in matrix:
        print(*row, sep=' ')