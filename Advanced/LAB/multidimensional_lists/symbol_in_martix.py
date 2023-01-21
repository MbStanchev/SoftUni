n = int(input())
matrix = []
found = False
for i in range(n):
    row = [x for x in input()]
    matrix.append(row)
symbol_to_search = input()

for row in range(n):
    if found:
        break
    for col in range(n):
        if symbol_to_search == matrix[row][col]:
            found = True
            print(f'({row}, {col})')
            break
if not found:
    print(f"{symbol_to_search} does not occur in the matrix")