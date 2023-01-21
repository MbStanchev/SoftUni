n, m = [int(x) for x in input().split(', ')]
matrix = []
r = 0
c = 0
res = []
biggest_sum = 0
for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])

for row in range(n - 1):
    for col in range(m - 1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            r = row
            c = col
for e in range(r, r + 1):
    for t in range(c, c +1):
        res.append(matrix[e][t])
print(f'{matrix[r][c]} {matrix[r][c+1]}')
print(f'{matrix[r+1][c]} {matrix[r+1][c+1]}')

print(biggest_sum)