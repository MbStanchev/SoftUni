rows, cols = [int(x) for x in input().split()]
snake = input()
matrix = []
ind = 0

for row in range(rows):
    current_row = []
    for col in range(cols):
        current_row.append(snake[ind % len(snake)])
        ind += 1
    if row % 2 == 0:
        print(*current_row, sep='')
    else:
        print(*reversed(current_row), sep='')
