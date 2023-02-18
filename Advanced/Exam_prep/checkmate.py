n = 8
queens = []
matrix = []
for _ in range(n):
    matrix.append(input().split())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "upright": (-1, 1),
    "downright": (1, 1),
    "upleft": (-1, -1),
    "downleft": (1, -1),
}
for row in range(len(matrix)):
    for cow in range(len(matrix)):
        if matrix[row][cow] == "Q":
            for d, step in directions.items():
                next_step_row = row + directions[d][0]
                next_step_cow = cow + directions[d][1]
                while True:
                    if 0 <= next_step_row < 8 and 0 <= next_step_cow < 8:

                        if matrix[next_step_row][next_step_cow] == "Q":
                            break
                        if matrix[next_step_row][next_step_cow] == "K":
                            queens.append([row, cow])
                            break
                        next_step_row += directions[d][0]
                        next_step_cow += directions[d][1]
                    else:
                        break
if queens:
    print(*queens, sep="\n")
else:
    print("The king is safe!")
