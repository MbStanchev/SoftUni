presents = int(input())
size = int(input())
matrix = []
santa_pos = ()
nice_kids = 0
presents_for_nice_kids = 0
out_of_presents = False
for i in range(size):
    matrix.append(input().split())
    for j in range(size):
        if matrix[i][j] == 'S':
            santa_pos = (i, j)
        if matrix[i][j] == 'V':
            nice_kids += 1
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    if command == 'Christmas morning':
        break
    matrix[santa_pos[0]][santa_pos[1]] = '-'
    next_pos_row = santa_pos[0] + directions[command][0]
    next_pos_col = santa_pos[1] + directions[command][1]
    if not (0 <= next_pos_row < len(matrix) and 0 <= next_pos_col < len(matrix)):
        continue
    santa_pos = (next_pos_row, next_pos_col)
    if matrix[santa_pos[0]][santa_pos[1]] == 'X':
        matrix[santa_pos[0]][santa_pos[1]] = '-'
        continue
    if matrix[santa_pos[0]][santa_pos[1]] == 'V':
        matrix[santa_pos[0]][santa_pos[1]] = '-'
        presents -= 1
        presents_for_nice_kids += 1

    elif matrix[santa_pos[0]][santa_pos[1]] == 'C':
        matrix[santa_pos[0]][santa_pos[1]] = '-'
        for direction in directions:
            give_presents_row = santa_pos[0] + directions[direction][0]
            give_presents_col = santa_pos[1] + directions[direction][1]
            if matrix[give_presents_row][give_presents_col] == 'V':
                matrix[give_presents_row][give_presents_col] = '-'
                presents -= 1
                presents_for_nice_kids += 1
            elif matrix[give_presents_row][give_presents_col] == 'X':
                matrix[give_presents_row][give_presents_col] = '-'
                presents -= 1
            if presents == 0 or presents_for_nice_kids == nice_kids:
                out_of_presents = True
                break

    matrix[santa_pos[0]][santa_pos[1]] = 'S'
    if out_of_presents or presents_for_nice_kids == nice_kids or presents == 0:
        break

if presents == 0 and presents_for_nice_kids < nice_kids:
    print('Santa ran out of presents!')
for row in matrix:
    print(*row, sep=' ')

if presents_for_nice_kids == nice_kids:
    print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids - presents_for_nice_kids} nice kid/s.')
