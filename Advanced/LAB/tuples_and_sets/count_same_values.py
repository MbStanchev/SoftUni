entry = (float(num) for num in input().split())

occ = {}
for num in entry:
    if num not in occ:
        occ[num] = 0
    occ[num] += 1

for num in occ.items():
    print(f'{num[0]} - {num[1]} times')