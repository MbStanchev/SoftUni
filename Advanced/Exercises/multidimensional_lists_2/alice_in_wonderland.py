n = int(input())
matrix = []
alice_pos = ()
tea_bags = 0
for r in range(n):
    matrix.append(input().split())
    for c in range(n):
        if matrix[r][c] == 'A':
            alice_pos = (r, c)
            matrix[r][c] = '*'

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while tea_bags < 10:
    direction = input()
    alice_next_pos_row = alice_pos[0] + directions[direction][0]
    alice_next_pos_col = alice_pos[1] + directions[direction][1]
    if not (0 <= alice_next_pos_row < len(matrix) and 0 <= alice_next_pos_col < len(matrix)):
        break
    alice_pos = (alice_next_pos_row, alice_next_pos_col)
    position = matrix[alice_next_pos_row][alice_next_pos_col]
    matrix[alice_next_pos_row][alice_next_pos_col] = '*'
    if position == 'R':
        break
    if position.isdigit():
        tea_bags += int(position)

if tea_bags >= 10:
    print("She did it! She went to the party.")
    for row in matrix:
        print(*row)
else:
    print("Alice didn't make it to the tea party.")
    for row in matrix:
        print(*row)