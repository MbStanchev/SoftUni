text = input()
counted_ch = {}
for ch in text:
    if ch not in counted_ch:
        counted_ch[ch] = 0
    counted_ch[ch] += 1
for letter, num in sorted(counted_ch.items()):
    print(f'{letter}: {num} time/s')
