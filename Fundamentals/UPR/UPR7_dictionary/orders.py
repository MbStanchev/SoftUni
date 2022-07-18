entry = input().split()
order = {}
while entry[0] != 'buy':
    drink = entry[0]
    price = float(entry[1])
    quontity = int(entry[2])

    if drink in order:
        order[drink] = [price, (quontity + order[drink][1])]
    else:
        order[drink]=[price, quontity]
    entry = input ().split()
for k in order:
    all = order[k][0]*order[k][1]
    print(f'{k} -> {all:.2f}')