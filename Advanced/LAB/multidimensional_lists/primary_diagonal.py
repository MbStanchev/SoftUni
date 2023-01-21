n = int(input())
matrix = []
res = []
row = 0
for i in range(n):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)

for row in range(n):
    suma = 0
    for col in range(n):
        if row == col:
            suma += matrix[row][col]
    res.append(suma)
print(sum(res))