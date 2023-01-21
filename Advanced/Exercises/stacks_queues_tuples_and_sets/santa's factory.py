from collections import deque
materials = [(int(x)) for x in input().split()]
magic_level = deque(int(x) for x in input().split())
presents = {150: 'Doll',
            250: 'Wooden train',
            300: 'Teddy bear',
            400: 'Bicycle'
}
crafted = {}
while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()
    result = current_material * current_magic

    if result in presents:
        toy = presents[result]
        if toy not in crafted:
            crafted[toy] = 0
        crafted[toy] += 1

    elif result < 0:
        materials.append(current_material + current_magic)

    elif result > 0:
        materials.append(current_material + 15)
    else:
        if current_magic == 0 and current_material == 0:
            continue

        if current_magic == 0:
            materials.append(current_material)

        elif current_material == 0:
            magic_level.appendleft(current_magic)

if ('Doll' in crafted and 'Wooden train' in crafted) or\
        ('Teddy bear' in crafted and 'Bicycle' in crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f'Materials left: {", ".join([str(x) for x in reversed(materials)])}')
if magic_level:
    print(f'Magic left: {", ".join([str(x) for x in magic_level])}')
for k,v in sorted(crafted.items()):
    print(f'{k}: {v}')

