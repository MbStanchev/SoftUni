from collections import deque
working_bees = deque(int(x) for x in input().split())
q_of_nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
result = 0

while working_bees and q_of_nectar and symbols:
    current_bee = working_bees[0]
    current_quantity = q_of_nectar[-1]
    current_symbol = symbols[0]
    if current_bee > current_quantity:
        current_quantity = q_of_nectar.pop()
        continue
    else:
        if current_quantity >= current_bee:
            if current_symbol == '-':
                result += abs(current_bee - current_quantity)
            elif current_symbol == '+':
                result += abs(current_bee + current_quantity)
            elif current_symbol == '*':
                result += abs(current_bee * current_quantity)
            elif current_symbol == '/' and current_quantity > 0:
                result += abs(current_bee / current_quantity)

            working_bees.popleft()
            q_of_nectar.pop()
            symbols.popleft()

print(f'Total honey made: {result}')
if working_bees:
    print(f'Bees left: {", ".join(str(x) for x in working_bees)}')
if q_of_nectar:
    print(f'Nectar left: {", ".join(str(x) for x in q_of_nectar)}')
