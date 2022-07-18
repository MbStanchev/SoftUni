entry = input().split()
priseles = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
obteined = False

while True:
    for i in range(0, len(entry), 2):

        quantity = int(entry[i])
        material = entry[i+1].lower()

        if material.lower() in priseles:
            priseles[material] += quantity
        elif material.lower() not in priseles:
            if material.lower() not in junk:
                junk[material] = 0
            junk[material] += quantity

        if priseles['shards'] >= 250:
            obteined = True
            priseles['shards'] -= 250
            print("Shadowmourne obtained!")
        elif priseles['fragments'] >= 250:
            obteined = True
            priseles['fragments'] -= 250
            print("Valanyr obtained!")
        elif priseles['motes'] >= 250:
            obteined = True
            priseles['motes'] -= 250
            print("Dragonwrath obtained!")
        if obteined:
            break
    if obteined:
        break

    entry = input().split()

for k,v in priseles.items():
    print(f'{k}: {v}')
for m, b in junk.items():
    print (f'{m}: {b}')