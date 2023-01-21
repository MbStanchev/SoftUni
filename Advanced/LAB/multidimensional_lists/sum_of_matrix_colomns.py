n, m = [int(x) for x in input().split(', ')]
result = []
matrix = []
row = 0
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for col in range(len(row)):
    sum_of_column = 0
    for row in range(n):
        sum_of_column += matrix[row][col]
    result.append(sum_of_column)

print(' '.join(str(x) for x in result))