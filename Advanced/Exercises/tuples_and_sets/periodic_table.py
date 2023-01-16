n = int(input())
chem_set = set()

for chem in range(n):
    chemical = input().split()
    chem_set = chem_set.union(chemical)
for el in chem_set:
    print(el)
