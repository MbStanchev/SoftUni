entry = input().split(' ')
dict = {}
for i in range(0, len(entry), 2):

    food = entry[i]
    quantity = entry[i + 1]
    dict[food] = int(quantity)
print(dict)