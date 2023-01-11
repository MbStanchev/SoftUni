usefull_items = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
legendary_item = False
speshal_item = ''
while not legendary_item:
    entry = input().split()
    for i in range(0, len(entry), 2):
        item_quantity = int(entry[i])
        item = entry[i + 1].lower()
        if item in usefull_items:
            usefull_items[item] += item_quantity
            if usefull_items[item] >= 250:
                legendary_item = True
                break
        else:
            if item not in junk:
                junk[item] = 0
            junk[item] += item_quantity

for item, quantity in usefull_items.items():
    if quantity >= 250:
        if item == 'shards':
            speshal_item = 'Shadowmourne'
            usefull_items['shards'] -= 250
        elif item == 'fragments':
            speshal_item = 'Valanyr'
            usefull_items['fragments'] -= 250
        elif item == 'motes':
            speshal_item = 'Dragonwrath'
            usefull_items['motes'] -= 250

print(f'{speshal_item} obtained!')
for k,v in usefull_items.items():
    print(f'{k}: {v}')
for k,v in junk.items():
    print(f'{k}: {v}')