n = int(input())

best_eggs = float('-inf')
best_dir = ''
path = []
matrix = []
bunny_pos = ()
for y in range(n):
    row = input().split()
    matrix.append(row)
    for z in range(n):
        if matrix[y][z] == 'B':
            bunny_pos = [y, z]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for direction in directions:
    sum_eggs = 0
    current_path = []
    r = bunny_pos[0] + directions[direction][0]
    c = bunny_pos[1] + directions[direction][1]

    while 0 <= r < len(matrix) and 0 <= c < len(matrix):
        if matrix[r][c] == 'X':
            break

        sum_eggs += int(matrix[r][c])
        current_path.append([r, c])
        r += directions[direction][0]
        c += directions[direction][1]

    if sum_eggs >= best_eggs:
        best_eggs = sum_eggs
        path = current_path
        best_dir = direction
if path:
    print(best_dir)
    print(*path, sep='\n')
    print(best_eggs)
