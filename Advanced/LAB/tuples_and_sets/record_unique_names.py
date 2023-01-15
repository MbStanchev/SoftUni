n = int(input())
set_as_set = set()

for i in range(n):
    names = input()
    set_as_set.add(names)
    # for name in set_as_set:
print('\n'.join(set_as_set))