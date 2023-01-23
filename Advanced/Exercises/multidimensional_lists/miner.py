def command_input(row, col, command):

    if command == 'left':
        return row, col - 1

    elif command == 'right':
        return row, col + 1

    elif command == 'up':
        return row - 1, col

    elif command == 'down':
        return row + 1, col


def is_in(row_to_chek, col_to_chek, matrix):
    if 0 <= row_to_chek < len(matrix) and 0 <= col_to_chek < len(matrix):
        return True


n = int(input())

matrix = []
commands = input().split()
current_row = 0
current_col = 0
total_col = 0

for rows in range(n):
    row = input().split()
    matrix.append(row)

    for col in range(n):
        if matrix[rows][col] == 's':
            current_row = rows
            current_col = col
        elif matrix[rows][col] == 'c':
            total_col += 1

for command in commands:

    next_row, next_col = command_input(current_row, current_col, command)
    if not is_in(next_row, next_col, matrix):
        continue
    else:
        if matrix[next_row][next_col] == 'e':
            print(f'Game over! ({next_row}, {next_col})')
            break
        if matrix[next_row][next_col] == 'c':
            total_col -= 1
            matrix[next_row][next_col] = '*'
            current_row = next_row
            current_col = next_col
            if total_col == 0:
                print(f'You collected all coal! ({current_row}, {current_col})')
                break
        else:
            current_row = next_row
            current_col = next_col
else:
    print(f'{total_col} pieces of coal left. ({current_row}, {current_col})')