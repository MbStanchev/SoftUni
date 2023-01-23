rows, cols = [int(x) for x in input().split()]
matrix = []
for i in range(rows):
    matrix.append([int(x) for x in input().split()])
best_row = 0
best_col = 0
maximal = float('-inf')
# biggest_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        # f_row = matrix[row][col:col + 3]
        # s_row = matrix[row + 1][col:col + 3]
        # t_row = matrix[row + 2][col:col + 3]
        # current_sum = sum(f_row) + sum(s_row) + sum(t_row)
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
                      matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
                      matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if current_sum > maximal:
            maximal = current_sum
            best_row = row
            best_col = col
            # biggest_matrix = [f_row, s_row, t_row]

print(f'Sum = {maximal}')
print(matrix[best_row][best_col], matrix[best_row][best_col + 1], matrix[best_row][best_col + 2])
print(matrix[best_row + 1][best_col], matrix[best_row + 1][best_col + 1], matrix[best_row + 1][best_col + 2])
print(matrix[best_row + 2][best_col], matrix[best_row + 2][best_col + 1], matrix[best_row + 2][best_col + 2])
