from collections import deque

total_pizzas = 0
pizza_orders = deque([int(x) for x in input().split(', ') if 0 < int(x) < 11])
employees = [int(x) for x in input().split(', ')]

while True:
    if not pizza_orders or not employees:
        break
    emp = employees[-1]
    pizza = pizza_orders[0]
    if employees[-1] < pizza_orders[0]:
        while employees[-1] < pizza_orders[0]:
            total_pizzas += employees[-1]
            pizza_orders[0] -= employees[-1]
            employees.pop()
            if not pizza_orders or not employees:
                break
    elif employees[-1] >= pizza_orders[0]:
        total_pizzas += pizza_orders[0]
        employees.pop()
        pizza_orders.popleft()

if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas}')
    print(f'Employees: {", ".join(str(x) for x in employees)}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(str(x) for x in pizza_orders)}')