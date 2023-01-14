from collections import deque
quantity_of_the_food = int(input())
orders = deque([int(x) for x in input().split()])
print(max(orders))
done = True
while orders:
    if quantity_of_the_food < orders[0]:
        done = False
        break
    else:
        quantity_of_the_food -= orders.popleft()
if done:
    print('Orders complete')
else:
    print('Orders left: ', end='')
    for order in orders:
        print(f'{order}', end=" ")