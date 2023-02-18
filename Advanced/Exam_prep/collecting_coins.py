# def index_check(row, cow, matrix):
#     if row < 0:
#         row = len(matrix) - 1
#     if cow < 0:
#         cow = len(matrix) - 1
#
#     if row >= len(matrix):
#         row = 0
#     if cow >= len(matrix):
#         cow = 0
#     return row, cow

deam = True
n = int(input())
matrix = []
player_pos = ()
coins_collected = 0
path = []
# wall = False
for r in range(n):
    row = input().split()
    matrix.append(row)
    for c in range(n):
        if matrix[r][c] == "P":
            player_pos = (r, c)
            path.append([r, c])
            matrix[r][c] = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
while coins_collected < 100:
    command = input()
    next_step_row = player_pos[0] + directions[command][0]
    next_step_col = player_pos[1] + directions[command][1]

    if next_step_row < 0:
        next_step_row = len(matrix) + next_step_row
    if next_step_col < 0:
        next_step_col = len(matrix) + next_step_col

    if next_step_row >= len(matrix):
        next_step_row = 0
    if next_step_col >= len(matrix):
        next_step_col = 0

    # next_step_row, next_step_col = index_check(next_step_row, next_step_col, matrix)
    player_pos = next_step_row, next_step_col
    path.append([next_step_row, next_step_col])
    if matrix[next_step_row][next_step_col] == "X":
        deam = False
        coins_collected = coins_collected // 2
        break
    else:
        coin = matrix[next_step_row][next_step_col]
        coins_collected += int(coin)
        matrix[next_step_row][next_step_col] = 0

if coins_collected >= 100:
    print(f"You won! You've collected {coins_collected} coins.")

elif not deam:
    print(f"Game over! You've collected {coins_collected} coins.")

print('Your path:')
print(*path, sep='\n')
