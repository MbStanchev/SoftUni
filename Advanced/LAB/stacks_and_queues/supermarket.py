from collections import deque

entry = input()
line = deque()

while not entry == 'End':
    if not entry == 'Paid':
        line.append(entry)
        entry = input()
    else:
        for i in range(len(line)):
            print(line.popleft())
        entry = input()
print(f'{len(line)} people remaining.')