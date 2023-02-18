def is_it_in(row, col, n, m):
    return 0 <= row < n and 0 <= col < m


n, m = [int(x) for x in input().split()]

matrix = []
player_pos = ()

players = 3
touched_opponents = 0
moves = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for row in range(n):
    r = input().split()
    matrix.append(r)
    for cow in range(m):
        if matrix[row][cow] == "B":
            player_pos = (row, cow)
            matrix[row][cow] = "-"

while True:
    if players == 0:
        break
    command = input()
    if command == 'Finish':
        break
    next_step_row = player_pos[0] + directions[command][0]
    next_step_cow = player_pos[1] + directions[command][1]
    # if not 0 > next_step_row >= n and not 0 > next_step_cow >= m:
    #     continue
    if not is_it_in(next_step_row, next_step_cow, n, m):
        continue
    if matrix[next_step_row][next_step_cow] == "O":
        continue

    if matrix[next_step_row][next_step_cow] == "P":
        matrix[next_step_row][next_step_cow] = "-"
        moves += 1
        players -= 1
        touched_opponents += 1
        player_pos = (next_step_row, next_step_cow)

    elif matrix[next_step_row][next_step_cow] == "-":
        player_pos = (next_step_row, next_step_cow)
        moves += 1

print("Game over!")
print(f'Touched opponents: {touched_opponents}', end=' ')
print(f'Moves made: {moves}')
