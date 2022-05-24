n = int(input())

counter = 1
printed = False
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(counter, end=" ")
        counter += 1
        if counter > n:
            printed = True
            break
    if printed:
        break
    print()