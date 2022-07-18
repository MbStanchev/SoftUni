entry = input().split()
dict = {}
for i in entry:
    i_lower = i.lower ()
    if i_lower not in dict:
        dict[i_lower] = 0
    dict[i_lower] += 1

for k in dict:
    if dict[k] % 2 != 0:
        print(k, end=' ')