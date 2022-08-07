import re
ready = {}
counter = 0
to_print = []
text = input()
pattern = r'(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
mirror_images = re.finditer(pattern, text)


for mach in mirror_images:
    counter += 1
    if mach[2] == mach[3][::-1]:
        ready[mach[2]] = mach[3]


if counter > 0:
    print(f'{counter} word pairs found!')
else:
    print("No word pairs found!")
if len(ready) > 0:
    print('The mirror words are:')
    for k,v in ready.items():
        to_print.append(f'{k} <=> {v}')
    print(", ".join(to_print))
else:
    print('No mirror words!')

