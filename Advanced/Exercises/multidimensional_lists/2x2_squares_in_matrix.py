n, m = [int(x) for x in input().split()]
matrix = []
even = 0
for i in range(n):
    matrix.append([x for x in input().split()])
for r in range(n-1):
    for c in range(m-1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            even += 1
print(even)