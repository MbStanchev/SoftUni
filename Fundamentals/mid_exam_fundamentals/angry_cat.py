price_raitings = list(map(int,input().split(', ')))
entry_point = int(input())
stat = input()
left = []
right = []
to_compare = price_raitings[entry_point]
for i in range(0, entry_point):
    if stat == 'cheap':
        if price_raitings[i] <= to_compare:
            left.append(price_raitings[i])
    elif stat == 'expensive':
        if price_raitings[i] >= to_compare:
            left.append(price_raitings[i])

for f in range(entry_point+1, len(price_raitings)):
    if stat == 'expensive':
        if price_raitings[f] >= to_compare:
            right.append(price_raitings[f])
    elif stat == 'cheap':
        if price_raitings[f] <= to_compare:
            right.append(price_raitings[f])

if sum(left) == sum(right):
    print(f'Left - {sum(left)}')
else:
    if sum(left) > sum(right):
        print(f'Left - {sum(left)}')
    else:
        print(f'Right - {sum(right)}')