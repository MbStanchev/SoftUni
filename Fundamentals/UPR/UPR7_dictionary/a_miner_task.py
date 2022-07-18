entry = input()
di = {}
while entry != 'stop':
    mineral = entry
    quantity = input()

    if mineral not in di:
        di[mineral] = 0
    di[mineral] += int(quantity)
    entry = input()
for mineral, quantity in di.items():
    print(f'{mineral} -> {quantity}')
