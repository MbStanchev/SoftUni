n = int(input())
row = 1
odd = set()
even = set()
for i in range(n):
    name_as_ord = []
    names = input()
    for ch in names:
        name_as_ord.append(int(ord(ch)))
    result = sum(name_as_ord) // (i + 1)
    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)

if sum(odd) == sum(even):
    print(f'{", ".join(str(y) for y in odd.union(even))}')
elif sum(odd) > sum(even):
    print(f'{", ".join(str(y) for y in odd.difference(even))}')
elif sum(odd) < sum(even):
    print(f'{", ".join(str(y) for y in odd.symmetric_difference(even))}')
