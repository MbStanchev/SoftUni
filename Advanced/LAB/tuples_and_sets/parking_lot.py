n = int(input())
set_as_set = set()
for i in range(n):
    op, num = input().split(', ')
    if op == 'IN':
        set_as_set.add(num)
    elif op == 'OUT':
        set_as_set.discard(num)
if not set_as_set:
    print("Parking Lot is Empty")
else:
    for num in set_as_set:
        print(num)