from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])
milkshake = 0
while cups_of_milk and chocolates and milkshake < 5:
    choko = chocolates.pop()
    milk = cups_of_milk.popleft()

    if choko <= 0 and milk <= 0:
        continue

    elif choko <= 0:
        cups_of_milk.appendleft(milk)
        continue

    elif milk <= 0:
        chocolates.append(choko)
        continue

    elif choko == milk:
        milkshake += 1
    else:
        cups_of_milk.append(milk)
        chocolates.append(choko - 5)
if milkshake == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")
if chocolates:
    print(f'Chocolate: {", ".join(str(x) for x in chocolates)}')
else:
    print(f'Chocolate: empty')
if cups_of_milk:
    print(f'Milk: {", ".join(str(x) for x in cups_of_milk)}')
else:
    print(f'Milk: empty')
