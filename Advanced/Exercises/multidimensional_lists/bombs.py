def is_it_in(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_neighbors(row, col, matrix):
    size = len(matrix)
    neighbors = []
    if is_it_in(row - 1, col, size) and matrix[row - 1][col] > 0:
        neighbors.append([row - 1, col])

    if is_it_in(row + 1, col, size) and matrix[row + 1][col] > 0:
        neighbors.append([row + 1, col])

    if is_it_in(row, col - 1, size) and matrix[row][col - 1] > 0:
        neighbors.append([row, col - 1])

    if is_it_in(row, col + 1, size) and matrix[row][col + 1] > 0:
        neighbors.append([row, col + 1])

    if is_it_in(row - 1, col - 1, size) and matrix[row - 1][col - 1] > 0:
        neighbors.append([row - 1, col - 1])

    if is_it_in(row + 1, col + 1, size) and matrix[row + 1][col + 1] > 0:
        neighbors.append([row + 1, col + 1])

    if is_it_in(row + 1, col - 1, size) and matrix[row + 1][col - 1] > 0:
        neighbors.append([row + 1, col - 1])

    if is_it_in(row - 1, col + 1, size) and matrix[row - 1][col + 1] > 0:
        neighbors.append([row - 1, col + 1])
    return neighbors


n = int(input())

matrix = []

for i in range(n):
    matrix.append([int(x) for x in input().split()])

bomb_cord = []
coordinates = input().split()
for el in coordinates:
    bomb_cord.append([int(x) for x in el.split(',')])

for bombs in bomb_cord:
    bomb_row, bomb_col = bombs
    if matrix[bomb_row][bomb_col] <= 0:
        continue

    bomb_power = matrix[bomb_row][bomb_col]
    neighbors = get_neighbors(bomb_row, bomb_col, matrix)

    for el in neighbors:
        matrix[el[0]][el[1]] -= bomb_power
    matrix[bomb_row][bomb_col] = 0
alive = 0
alive_sum = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] > 0:
            alive += 1
            alive_sum += matrix[row][col]
print(f'Alive cells: {alive}')
print(f'Sum: {alive_sum}')
for row in matrix:
    print(*row, sep = ' ')
 