row, columns = [int(x) for x in input().split(', ')]
matrix = []
total_sum = 0
for i in range(row):

    matrix.append([int(x) for x in input().split(', ')])
    total_sum += sum(matrix[i])

print(total_sum)
print(matrix)