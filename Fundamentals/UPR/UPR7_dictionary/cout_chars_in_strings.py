entry1 = input()
chars = {}
entry = entry1.replace(' ', '')
for i in range(0, len(entry)):
    if entry[i] not in chars:
        chars[entry[i]] = 0
    chars[entry[i]] += 1
for letter, valiue in chars.items():
    print(f'{letter} -> {valiue}')