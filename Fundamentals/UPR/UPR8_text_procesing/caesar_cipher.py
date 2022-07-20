entry = input().split()
real = ' '.join(entry)
result = ''
mid = 0
for ch in real:
    mid = ord(ch)
    result += chr(mid + 3)

print(result)