n = int(input())
matrix = []
primary = []
secondary = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])

for i in range(n):
    for j in range(n):
        if i == j:
            primary.append(matrix[i][j])
        if (i + j) == (n - 1):
            secondary.append(matrix[i][j])
print(f'Primary diagonal: {", ".join(str(x) for x in primary)}. Sum: {sum(primary)}')
print(f'Secondary diagonal: {", ".join(str(y) for y in secondary)}. Sum: {sum(secondary)}')